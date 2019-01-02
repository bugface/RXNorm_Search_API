import logging


def create_logger(logger_name, logger_level='info', format='%(asctime)-15s %(message)s', filename=None):
    FORMAT = format
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(logger_name)
    if logger_level == 'debug':
        logger_level_setting = logging.DEBUG
    elif logger_level == 'info':
        logger_level_setting = logging.INFO
    elif logger_level == 'warning':
        logger_level_setting = logging.WARNING
    else:
        logger_level_setting = logging.ERROR
    logger.setLevel(logger_level_setting)
    return logger


REQUESTS_TIMEOUT=0.5