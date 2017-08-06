Zoho Reports
============

This project is a simple management interface for static web pages.  Users are
authenticated via OAuth2 against an Open edX installation.

The project is intended to embed Zoho reports on Cloudera's own domain.

Setting up the development environment
--------------------------------------

### pipenv

This project uses pipenv[1] to manage dependencies.  You first need to install
pipenv, e.g. using

    pip3 install --user pipenv

[1]: http://pipenv.org/

If you want to install pipenv in a separate virtualenv, see [fancy installation
of pipenv][2] for a way to do so.

[2]: http://docs.pipenv.org/en/latest/advanced.html#fancy-installation-of-pipenv

To set up a virtual environment and install the development requirements:

    pipenv install --dev

To run the tests:

    pipenv run tox

To enter a new shell inside the environment:

    pipenv shell

### Authenticating with an Open edX devstack

1. Start the Open edX devstack in standard configuration, with the LMS listening
   on http://localhost:8000/.

1. Navigate to http://localhost:8000/admin/oauth2/client/add/ to add a new
   OAuth2 client.  Use these settings:

   URL: http://localhost:9000/

   Redirect URI: http://localhost:9000/complete/edx-oidc/

   Client ID: zoho_reports

   Client secret: open_secret

   Client type: Confidential (Web applications)

   Logout URI: http://localhost:9000/logout

1. Start the zoho_reports development server using

       pipenv run python manage.py runserver

1. Navigate to http://localhost:9000/

1. Log in with a devstack account.
