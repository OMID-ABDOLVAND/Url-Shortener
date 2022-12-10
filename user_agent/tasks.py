from core.Celery import app
from user_agent.models import UserAgentModel


@app.task
def data_saver_task(os, browser, ip, url):
    try:
        obj = UserAgentModel.objects.create(ip=ip, os=os, browser=browser, url=url)
    except Exception as e:
        print(e)

def save_redirector_detail(request, url):
    os = request.user_agent.get_user_os
    browser = request.user_agent.get_user_browser
    ip = request.user_agent.get_user_ip
    data_saver_task.delay(os=os, browser=browser, ip=ip, url=url)
