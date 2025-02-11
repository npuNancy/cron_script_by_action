import os
import json
import logging
import logging.handlers

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


def send_msg():
    try:
        SOME_SECRET = os.environ["SOME_SECRET"]
    except KeyError:
        logger.error("SOME_SECRET not found in environment variables")
        return
    
    try:
        url = "http://www.pushplus.plus/send"
        body = SOME_SECRET.encode(encoding="utf-8")
        headers = {"Content-Type": "application/json"}
        requests.post(url, data=body, headers=headers)
        logger.info("Message sent successfully")
    except Exception as e:
        logger.error(f"Error sending message: {e}")

if __name__ == "__main__":
    logger.info(f"Starting script")
    send_msg()
