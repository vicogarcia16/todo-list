from db.database import SessionLocal
from db.models import Task
from datetime import datetime, timezone

def load_tasks():
    with SessionLocal() as session:
        return session.query(Task).all()

def save_task(task):
    with SessionLocal() as session:
        session.add(task)
        session.commit()

def delete_task(checked_ids):
    with SessionLocal() as session:
        tasks_to_delete = session.query(Task).filter(Task.id.in_(checked_ids)).all()
        for task_to_delete in tasks_to_delete:
            session.delete(task_to_delete)
        session.commit()
