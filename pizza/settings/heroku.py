from .base import *

import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['cs50w-proj3-pizza.herokuapp.com']

# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
