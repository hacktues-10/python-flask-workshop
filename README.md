# Въведение в Python и Flask

[![Въведение в Python и Flask – Калоян Миладинов и Божидар Павлов (Hack TUES X Workshop #3)](https://img.youtube.com/vi/eEodMLM3RY0/0.jpg "Гледай записа в YouTube")](https://youtube.com/watch?v=eEodMLM3RY0)

Тази лекция ще ви запознае с Flask - лек и мощен инструмент за създаване на уеб приложения с Python. Калоян и Божидар ще ви покажат как да започнете своите проекти с Flask, като напишат бакенда на приложение, подобно на ChatGPT, свързано с общодостъпния модел за генериране на текст, Llama 2.

## Ресурси

- [Презентацията](./docs/Python%20-%20Flask%20Presentation.pdf)
- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)
- [Документация на Python](https://docs.python.org/3/)
- [Видове заявки](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [The Flask Mega-Tutorial, Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Huggingface](https://huggingface.co/)
- [Huggingface space-ове](https://huggingface.co/spaces)
- [Huggingface NLP курс](https://huggingface.co/learn/nlp-course)

## Инструкции за пускане на проекта

> **Бележка:** Всичко при командите до `$` включително е част от prompt-а на командния ред. Не го копирайте като копирате команди от тук.

1. Създаване на Python виртуална среда *(ако не използвате PyCharm)*
```console
$ python -m venv venv
$ . venv/bin/activate
(venv) $
```

2. Инсталиране на зависимостите
```console
(venv) $ pip install -r requirements.txt
```

3. Стартиране на сървъра
```console
(venv) $ python app.py
```
