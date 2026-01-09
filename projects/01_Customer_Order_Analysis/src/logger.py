import logging


def get_logger(name):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s %(message)s",
        datefmt=("%Y-%m-%d %H:%M:%S"),
    )

    logger = logging.getLogger(name)
    return logger
