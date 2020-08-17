
### Set up Virtual Environment

```console
python3 -m venv venv
$ source venv/bin/activate
```

### Install necessary packages

```console
(venv) $ pip install -r requirements.txt
```
### If that commands fails, these are the packages used to run the app:

```console
pip3 install flask
pip3 install psycopg2
pip3 install flask_sqlalchemy
pip3 install flask_bcrypt
pip3 install email_validator
pip3 install flask_wtf
pip3 install lsqlalchemy
pip3 install flask_debugtoolbar
```

### Set up the Database

```console
(venv) $ createdb warbler
(venv) $ python seed.py
```

### Start the app

```console
flask run
```


### About g object

g is an object provided by Flask. It is a global namespace for holding any data you want during a single app context. For example, a before_request handler could set g.user, which will be accessible to the route and other functions.

Useful [link](https://flask.palletsprojects.com/en/1.1.x/appcontext/#storing-data)

