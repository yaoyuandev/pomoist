from todoist_api_python.api import TodoistAPI
import config
from furl import furl

api = TodoistAPI(config.token)


def comment(content, id):
    comment = api.add_comment(
        content=content,
        task_id=id
    )
    print(comment)


def get_id(s):
    f = furl(s)
    return f.args['id']
