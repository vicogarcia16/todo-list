import flet as ft
from db.db_task import save_task

def add_task_to_column(page, task_column, task):
    checkbox = ft.Checkbox(label=task["label"], value=task["completed"])

    def checkbox_changed(e):
        task["completed"] = checkbox.value
        save_task(task)

    checkbox.on_change = checkbox_changed

    task_panel = ft.Card(
        content=ft.Container(
            content=ft.Row(controls=[checkbox], alignment="start"),
            padding=10
        ),
        margin=ft.Margin(left=25, top=10, right=30, bottom=-10)
    )

    task_panel.task_id = task["id"]
    task_panel.checkbox = checkbox
    task_column.controls.append(task_panel)
    page.update()
