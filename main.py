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
        logger.error("SOME_SECRET 未设置")
        return
    
    try:
        url = "http://www.pushplus.plus/send"
        body = SOME_SECRET.encode(encoding="utf-8")
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, data=body, headers=headers)

        if res.status_code == 200:
            logger.info("√ 用户消息推送成功！")
        else:
            logger.error(f"X 推送消息提醒失败！")

    except Exception as e:
        logger.error(f"错误: {e}")

if __name__ == "__main__":
    logger.info(f"开始执行脚本")
    send_msg()
