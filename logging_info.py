import logging
import os  # not used -- just avoiding linter-irritation

## basic logging ---------------------------------------------------

"""
From a `main.py` file, somewhere near the top.
- Shows the logging `format` I really like.
- Shows optional file-logging.
"""

# log_dir: Path = stuff_dir / 'logs'
# log_dir.mkdir(parents=True, exist_ok=True)  # creates the log-directory inside the stuff-directory if it doesn't exist
# log_file_path: Path = log_dir / 'auto_updater.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    # filename=log_file_path,
)
log = logging.getLogger(__name__)


## django logging ---------------------------------------------------

"""
From a django settings.py file, the public-repo settings.

Main thing:
- Shows the logging `format` I really like.

Also:
- Explicates the relationship between loggers and handlers.
- Shows a good use of `environ.get()` (I normally _really_ prefer quick-failing `environ['FOO']`).
- Includes reminder of cool inspectable sql-output.
"""

## reminder:
## "Each 'logger' will pass messages above its log-level to its associated 'handlers',
## ...which will then output messages above the handler's own log-level."
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'logfile': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),  # add LOG_LEVEL=DEBUG to the .env file to see debug messages
            'class': 'logging.FileHandler',  # note: configure server to use system's log-rotate to avoid permissions issues
            'filename': os.environ['LOG_PATH'],
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'pdf_checker_app': {
            'handlers': ['logfile'],
            'level': 'DEBUG',  # messages above this will get sent to the `logfile` handler
            'propagate': False,
        },
        # 'django.db.backends': {  # re-enable to check sql-queries! <https://docs.djangoproject.com/en/5.2/ref/logging/#django-db-backends>
        #     'handlers': ['logfile'],
        #     'level': os.environ['LOG_LEVEL'],
        #     'propagate': False
        # },
    },
}
