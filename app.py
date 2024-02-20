from datetime import datetime

import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

app = flask.Flask(__name__)


@app.route('/')
def index():
    # Copilot generated this:
    return '<marquee>Съли е най-добрият!</marquee>'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

db = SQLAlchemy(app)


class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    is_liked: Mapped[bool] = mapped_column(default=False)
    is_from_user: Mapped[bool] = mapped_column(default=True)

    def to_dict(self):
        result = {
            'id': self.id,
            'text': self.text,
            'created_at': self.created_at,
            'is_liked': self.is_liked
        }
        if self.is_from_user:
            result['from'] = 'Вие'
            result['avatar'] = '<URL на профилната снимка на потребителя>'
        else:
            result['from'] = 'Съли'
            result['avatar'] = '<URL на профилната снимка на Съли>'
        return result


@app.get('/messages')
def get_messages():
    messages = Message.query.all()
    return [message.to_dict() for message in messages]


@app.post('/messages')
def create_message():
    text = flask.request.json['text']
    user_message = Message(text=text)

    # TODO: Добави AI тук
    sully_message = Message(text='🤫', is_from_user=False)

    db.session.add(user_message)
    db.session.add(sully_message)
    db.session.commit()

    return [user_message.to_dict(), sully_message.to_dict()]


@app.delete('/messages')
def clear_message_history():
    Message.query.delete()
    db.session.commit()
    return '', 204


@app.patch('/messages/<int:message_id>')
def like_message(message_id):
    is_liked = flask.request.json['is_liked']

    message = Message.query.get_or_404(message_id)
    if not message.is_from_user:
        message.is_liked = is_liked

    db.session.commit()
    return message.to_dict()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Създава таблиците в базата данни, ако не съществуват
    app.run(debug=True)
