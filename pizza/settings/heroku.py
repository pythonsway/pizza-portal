from .base import *

import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['cs50w-proj3-pizza.herokuapp.com']

# # Heroku: Update database configuration from $DATABASE_URL.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}
