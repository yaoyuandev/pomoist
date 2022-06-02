from todoist_api_python.api import TodoistAPI
from config import config
from furl import furl
import datetime

config = config()
api = TodoistAPI(config['token'])


def comment(content, id):
    comment = api.add_comment(
        content=content,
        task_id=id
    )
    print(comment)


def get_id(s):
    f = furl(s)
    return f.args['id']


def get_task(id):
    task = api.get_task(id)
    project = api.get_project(task.project_id)
    root = None
    if project.parent_id != None:
        root = api.get_project(project.parent_id)
    return {"task": task, "project": project, "root": root}


def get_task_by_url(url):
    return get_task(int(get_id(url)))


def due_today(id):
    try:
        is_success = api.update_task(task_id=id, due_string='today')
        print(is_success)
    except Exception as error:
        print(error)
