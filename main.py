import flet as ft
from db.db_task import load_tasks
from config.page import config_page_sf
from ui.task_ui import add_task_to_column
from ui.buttons_ui import create_control_panel, create_close_button

def main(page: ft.Page):
    page.title = "TODO List"
    config_page_sf(page)

    tasks = load_tasks()  # Cargar las tareas desde la base de datos
    task_column = ft.Column()

    # Crear los botones
    control_panel = create_control_panel(page, task_column)
    close_button = create_close_button(page)

    # Cargar tareas previamente guardadas de la base de datos
    for task in tasks:
        add_task_to_column(page, task_column, task)

    # Organizar la interfaz
    page.add(
        ft.Column(
            controls=[
                control_panel,  # Controles arriba
                task_column,    # Columna de tareas
                close_button    # Botón de cerrar ventana
            ],
            expand=True,
        )
    )

ft.app(target=main)
