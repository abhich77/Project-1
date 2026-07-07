from src.logger import logging

logging.debug("testing logger")

from src.exception import MYException
import sys

try:
    a=1+"z"
except Exception as e:
    logging.info(e)
    raise MYException(e,sys) from e