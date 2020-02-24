import os

from flask_appbuilder.security.manager import AUTH_OAUTH
from airflow.configuration import conf

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')

CSRF_ENABLED = True

AUTH_TYPE = AUTH_OAUTH

AUTH_ROLE_ADMIN = 'Admin'

AUTH_USER_REGISTRATION = True

AUTH_USER_REGISTRATION_ROLE = "User"

OAUTH_PROVIDERS = [{
    'name': 'google',
    'whitelist': ['@example.com'],
    'token_key': 'access_token',
    'icon': 'fa-google',
    'remote_app': {
        'base_url': 'https://www.googleapis.com/oauth2/v2/',
        'request_token_params': {
            'scope': 'email profile'
        },
        'access_token_url': 'https://accounts.google.com/o/oauth2/token',
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'request_token_url': None,
        'consumer_key': os.getenv('AIRFLOW_GOOGLE_OAUTH_KEY'),
        'consumer_secret': os.getenv('AIRFLOW_GOOGLE_OAUTH_SECRET'),
    }
}]
