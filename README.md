Here are some set up instrunctions after this repo is has been cloned to your local machine.

## Installation

This project uses pipenv as it's package manager.

If you do not have pipenv on your machine:

```bash
brew install pipenv
```
or
```
pip install pipenv
```

Then install pacakges with pipenv

```bash
pipenv install
```

## Initialize the Data Base

This project uses PostgreSQL as it's db, so with postgres server running on your machine run:

```bash
createdb example
```

Then run the schem migration with:
```bash
pipenv run flask db upgrade
```

Then seed the db by running:
```bash
pipenv run python3 ./seed.py
```

## Running the app

Use this command to run the flask server:

```bash
pipenv run flask run
```

Then navigate in your browser to http://localhost:5000/graphql to access the GraphiQL inerface
