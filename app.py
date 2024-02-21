import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sully import Sully

sully = Sully()
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"

db = SQLAlchemy(app)


class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    is_from_user: Mapped[bool] = mapped_column(default=True)
    is_liked: Mapped[bool] = mapped_column(default=False)

    def to_json(self):
        result = {
            'id': self.id,
            'text': self.text,
            'is_liked': self.is_liked,
        }
        if self.is_from_user:
            result['from'] = 'Вие'
            result['avatar'] = 'https://hacktues.bg/workshop/user.png'
        else:
            result['from'] = 'Съли'
            result['avatar'] = 'https://hacktues.bg/workshop/sully.png'
        return result


@app.get('/')
def hello():
    return 'Hello, world!'


@app.get('/messages')
def read_history():
    messages = Message.query.all()
    results = []
    for message in messages:
        results.append(message.to_json())
    return results


@app.post('/messages')
def create_message():
    text = flask.request.json['text']
    user_message = Message(text=text)

    output = sully.prompt(text)
    sully_message = Message(text=output, is_from_user=False)

    db.session.add(user_message)
    db.session.add(sully_message)
    db.session.commit()
    
    return [user_message.to_json(), sully_message.to_json()]

@app.delete('/messages')
def clear_message_history():
    Message.query.delete()
    db.session.commit()
    return '', 204

@app.patch('/messages/<int:message_id>')
def like_message(message_id):
    message = Message.query.get_or_404(message_id)

    is_liked = flask.request.json['is_liked']

    if is_liked:
        message.is_liked = True
    else:
        message.is_liked = False

    db.session.commit()

    return message.to_json()


with app.app_context():
    db.create_all()
app.run(debug=True, use_reloader=False)