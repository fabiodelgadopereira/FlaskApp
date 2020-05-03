import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROPAGATE_EXCEPTIONS = True # To allow flask propagating exception even if debug is set to false on app
JWT_AUTH_HEADER_PREFIX = 'Bearer'
APP_NAMME = 'FlaskApp'
