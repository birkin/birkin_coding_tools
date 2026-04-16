import logging
import os

# log_dir: Path = stuff_dir / 'logs'
# log_dir.mkdir(parents=True, exist_ok=True)  # creates the log-directory inside the stuff-directory if it doesn't exist
# log_file_path: Path = log_dir / 'auto_updater.log'
logging.basicConfig(
    level=logging.DEBUG if os.getenv('LOG_LEVEL') == 'DEBUG' else logging.INFO,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    # filename=log_file_path,
)
log = logging.getLogger(__name__)


def main():
    log.info('Hello from gather-repos-code!')


if __name__ == '__main__':
    main()
