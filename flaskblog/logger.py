import logging


def configure_logger():
    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(logging.DEBUG)

    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')
    console_logger.setFormatter(formatter)

    app_logger.addHandler(console_logger)

    return app_logger


logger = configure_logger()
