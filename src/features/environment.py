import logging

def before_all(context):
    context.config.setup_logging(level=logging.DEBUG,configfile="behave.ini")
