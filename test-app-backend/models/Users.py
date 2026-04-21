import uuid
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.sql import func
from core.database import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True, unique=True, index=True)
    email = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    status = Column(String, nullable=False, default='active')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __init__(self, email, password):
        self.user_id = f"USER{uuid.uuid4().int % 10000000}"
        self.email = email
        self.password = password