from sqlalchemy import String, Integer, DateTime, Column
from app.database import Base
from enum import Enum
from datetime import datetime, timezone


class TaskEnum(str, Enum):
    pending = "pending"
    done = "done"

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default=TaskEnum.pending.value, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
