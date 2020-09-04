Zoho Reports
============

This project is a simple management interface for static web pages.  Users are
authenticated via OAuth2 against an Open edX installation.

The project is intended to embed Zoho reports on Cloudera's own domain.

Setting up the development environment
--------------------------------------

### pipenv

This project uses [pipenv][1] to manage dependencies.  You first need to install
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
   on http://localhost:18000/.

1. Navigate to http://localhost:18000/admin/oauth2_provider/application/add/ to add a new
   OAuth2 client. Use these settings:
   - Client id: zoho_reports
   - Redirect uris: http://localhost:9000/complete/edx-oauth2/
   - Client type: Confidential
   - Authorization grant type: Authorization code
   - Client secret: open_secret
   - Name: zoho_reports

1. Navigate to http://localhost:18000/admin/oauth_dispatch/applicationaccess/add/ to add
   access for the new Oauth2 client.  Use these settings:
   - Application: zoho_reports
   - Scopes: user_id,profile,email

1. Start the zoho_reports development server using

       pipenv run python manage.py runserver 9000

1. Navigate to http://localhost:9000/.

1. Log in with a devstack account.
