
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

### Explore database

```console
psql warbler
```

also you can test the models by inserting statements through ipython:
```console
ipython
```

### About g object

Flask provides us with the object [g]((https://flask.palletsprojects.com/en/1.1.x/appcontext/#storing-data)). It is a global namespace for holding any data you want during a single app context. The g stands for global, but that is referring to being global within a contect. 

For example, a before_request handler could set g.user, which will be accessible to the route and other functions.

So, it's basically a global object to which we can add our logged in user object in order to freely use it across different routes (globally in our Flask app).

Therefore, we create the add_user_to_g route which will check the session for the user id (which gets set upon successful login) and if it can find it it will set it to g.user (to make the user object available globally). If it can't find it, g.user is set to None which means there isn't a user currently logged in.


Then, whenever you need to access the logged in user object you don't have to rewrite a query to find it in the database, you can just access it from g.user

The [before_request decorator](https://pythonise.com/series/learning-flask/python-before-after-request) allows us to create a function that will run before each request (it will run that function which should define g.user before every request sent to your Flask app)


