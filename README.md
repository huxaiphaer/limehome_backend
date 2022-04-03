# Limehome Sample Backend.

This is the hotel reservation backend application.


###  Requirements for setting up the project.
1. Python3.
2. Django
3. Virtualenv.
4. Postgres DB
5. Heroku.


### Installation on Mac/Linux

1 . First clone this repository

```
$ https://github.com/huxaiphaer/limehome_backend.git
```

2 . Add the following variables in your Environment Variables permanently `.env` file:

```

DATABASE_URL=postgresql://user:<password>@localhost:<port>/<db>
SECRET_KEY=any_secret_key
DEBUG_CONFIG=True
DEBUG=True

```

After, setting up the environment variables add create a Postgres Database, followed by running  migrations with the commands
below to create all the necessary tables :

```
$  ./manage.py migrate
```

Then finally run :

```
$ ./manage.py runserver
```
