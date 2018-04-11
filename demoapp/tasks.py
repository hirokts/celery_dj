# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    time.sleep(10)
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def add_sec(x, y, sec):
    time.sleep(sec)
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y

# crontab設定でemailを送る
# 1時間に１回現時刻で送るメール設定があるかどうかをクエリで調べる
# 該当するメールを送信する
