import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Creating file handler which logs debug and higher level messages
    file_handler = logging.FileHandler('bot.log')
    file_handler.setLevel(logging.DEBUG)

    # Creating console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Creating formatter and adding it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adding handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger