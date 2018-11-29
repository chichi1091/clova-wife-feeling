```shell
$ python -m venv env
$ source env/bin/activate
$ pip install flask
$ pip install gunicorn
$ pip install clova-cek-sdk
$ pip freeze > requirements.txt
$ echo Python 3.6.6 > runtime.txt
$ echo web: gunicorn app:app --log-file=- > Procfile

$ touch server.py
```