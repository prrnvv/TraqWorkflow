import logging


def setup_logging(log_file="test_log.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] | %(levelname))s | %(filename)s | %(lineno)s | %(message)s)]')
    info_handler = logging.FileHandler(log_file)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(console_handler)
    logging.addLevelName(logging.DEBUG, "DEBUG")
    logging.addLevelName(logging.INFO, "INFO")
    logging.addLevelName(logging.WARNING, "WARNING")
    logging.addLevelName(logging.ERROR, "ERROR")
    logging.addLevelName(logging.CRITICAL, "CRITICAL")
    return logger
