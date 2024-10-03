from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base
from datetime import datetime, timezone

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now(timezone.utc))