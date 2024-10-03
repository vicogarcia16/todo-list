import flet as ft
from actions.task_actions import add_clicked, delete_checked_tasks
from db.db_task import load_tasks

def create_control_panel(page, task_column):
    new_task = ft.TextField(hint_text="What needs to be done?", width=225,
                            on_submit=lambda e: add_clicked(e, page, task_column, new_task))
    add_button = ft.IconButton(
        ft.icons.ADD_CIRCLE_OUTLINED,
        on_click=lambda e: add_clicked(e, page, task_column, new_task),
        icon_size=35,
        icon_color=ft.colors.BLUE
    )
    delete_button = ft.IconButton(
        ft.icons.DELETE_ROUNDED,
        on_click=lambda e: delete_checked_tasks(e, page, task_column, load_tasks()),
        icon_size=35,
        icon_color=ft.colors.GREEN
    )
    
    return ft.Container(
        content=ft.Row(
            controls=[new_task, add_button, delete_button],
            alignment="start"
        ),
        margin=ft.Margin(left=25, top=20, right=0, bottom=0)
    )

def create_close_button(page):
    close_button = ft.IconButton(
        ft.icons.CLOSE_OUTLINED,
        on_click=lambda e: page.window.close(),
        icon_size=35,
        icon_color=ft.colors.RED,
        visible=False  # Inicialmente oculto
    )

    def handle_hover(e):
        close_button.visible = e.data == "true"
        page.update()

    return ft.Container(
        content=close_button,
        alignment=ft.alignment.center,
        padding=5,
        on_hover=handle_hover,
        margin=ft.Margin(left=0, top=10, right=0, bottom=0)
    )
