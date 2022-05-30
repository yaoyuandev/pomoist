import todoist
import vika_api


def sync(url):
    id = int(todoist.get_id(url))
    todoist.comment('start', id)
    task = todoist.get_task(id)
    vika_api.insert(task['task'].content,
                    task['project'].name, task['root'].name, id)
