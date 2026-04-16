import logging
import sys


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "file_handler": { 
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 1024 * 1024 * 1, # = 1MB
            "backupCount": 3,
        },
    },
    
    "loggers": {
        "app": {"handlers": ["console", "file_handler"], "level": "DEBUG", "propagate": False},
    },
    #"root": {"handlers": ["console"], "level": "DEBUG"},
}