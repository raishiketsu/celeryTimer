import time
from celery_tasks.celery import cel

@cel.task
def send_email(res):
    print("向%s发送邮件完成" % res)
    time.sleep(5)
    return "完成向%s发送邮件任务"%res
