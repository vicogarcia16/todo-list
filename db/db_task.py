from db.database import get_db

def load_tasks():
    supabase = get_db()
    response = supabase.table('tasks').select('*').execute()
    return response.data

def save_task(task):
    supabase = get_db()
    # Verifica si la tarea ya tiene un ID
    if "id" in task and task["id"]:
        # Si la tarea existe, actualiza la tarea
        response = supabase.table('tasks').update(task).eq('id', task['id']).execute()
    else:
        # Si la tarea no tiene un ID, inserta la tarea
        response = supabase.table('tasks').insert(task).execute()
        # Obtén el ID asignado por la base de datos
        task["id"] = response.data[0]["id"]
    return task

def delete_task(checked_ids):
    supabase = get_db()
    for id in checked_ids:
        response = supabase.table('tasks').delete().eq('id', id).execute()
    return response
