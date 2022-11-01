import todoist
import vika_api


def sync(url):
    print(url)
    id = int(todoist.get_id(url))
    print(id)
    todoist.comment('start', id)
    todoist.label('now', id)
    task = todoist.get_task(id)
    print(task)
    if not task['task'].due or not task['task'].due.recurring:
        todoist.due_today(id)
    task_root_name = ''
    if task['root'] != None:
        task_root_name = task['root'].name

    vika_api.insert(task['task'].content,
                    task['project'].name, task_root_name, id)
