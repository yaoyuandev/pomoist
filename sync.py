import todoist
import vika_api


def sync(url):
    id = int(todoist.get_id(url))
    todoist.comment('start', id)
    task = todoist.get_task(id)
    if not task.due.recurring:
        todoist.due_today(id)
    task_root_name = ''
    if task['root'] != None:
        task_root_name = task['root'].name

    vika_api.insert(task['task'].content,
                    task['project'].name, task_root_name, id)
