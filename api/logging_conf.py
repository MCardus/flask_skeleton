"""Logging configuration"""

import os
import logging
import logging.config
import functools
import json
import yaml


def setup_logging(
        default_path='logging_properties.yml',
        default_level=logging.DEBUG,
        env_key='LOG_CFG'
):
    """Setup logging configuration"""

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    path = os.path.join(os.getcwd(), path)
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def log_func():
    """
    Decorator logging func name and args
    :return:
    """
    def func(func):
        @functools.wraps(func)
        def decorator(*args, **kwds):
            logging.debug(json.dumps({"method": func.__name__, "args": kwds}))
            f_result = func(*args, **kwds)
            return f_result
        return decorator
    return func


if __name__ == '__main__':
    logging.info("Hello World")
    logging.debug("Hello World")
    logging.error("Hello World")
