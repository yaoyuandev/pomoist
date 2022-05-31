import todoist
import vika_api


def sync(url):
    id = int(todoist.get_id(url))
    todoist.comment('start', id)
    todoist.due_today(id)
    task = todoist.get_task(id)
    task_root_name = ''
    if task['root'] != None:
        task_root_name = task['root'].name

    vika_api.insert(task['task'].content,
                    task['project'].name, task_root_name, id)
