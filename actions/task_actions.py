from db.db_task import save_task, load_tasks, delete_task
from ui.task_ui import add_task_to_column
from db import models

def add_clicked(e, page, task_column, new_task):
    label = new_task.value.strip()
    if label:
        task = models.Task(label=label, completed=False)
        save_task(task)
        task = load_tasks()[-1]
        add_task_to_column(page, task_column, task)
        new_task.value = ""
        page.update()

def delete_checked_tasks(e, page, task_column, tasks):
    checked_ids = []
    for task_panel in task_column.controls:
        checkbox = task_panel.checkbox
        if checkbox.value:
            task_id = task_panel.task_id
            checked_ids.append(task_id)

    delete_task(checked_ids)
    task_column.controls.clear()
    tasks.clear()
    tasks.extend(load_tasks())

    for task in tasks:
        if not task.completed:
            add_task_to_column(page, task_column, task)

    page.update()
