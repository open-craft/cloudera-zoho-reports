Zoho Reports
============

This project is a simple management interface for static web pages.  Users are
authenticated via OAuth2 against an Open edX installation.

The project is intended to embed Zoho reports on Cloudera's own domain.

Getting started
---------------

This project uses pipenv[1] to manage dependencies.  You first need to install
pipenv, e.g. using

    pip install --user pipenv

[1]: http://pipenv.org/

To set up a virtual environment and install the development requirements:

    pipenv install --dev

To run the tests:

    pipenv run tox

To enter a new shell inside the environment:

    pipenv shell
