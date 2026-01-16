from pydantic import BaseModel, ConfigDict, Field
from typing import List
from uuid import UUID, uuid4
from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base
import uuid

class Todo(BaseModel):
    uuid: UUID = Field(default_factory=lambda: uuid4())
    title: str
    description: str
    parent_uuid: UUID | None = None

    def __repr__(self):
        return f"Todo(id={self.uuid}, title={self.title}, description={self.description}, parent_id={self.parent_uuid})"

    model_config = ConfigDict(arbitrary_types_allowed=True)


class TodoWithChildren(Todo):
    children: List[UUID] = []

class TodoDB(Base):
    __tablename__="todos"

    uuid=Column(String,primary_key=True,default=lambda: str(uuid.uuid4()))
    title=Column(String,index=True)
    descriptionn=Column(String)
    parent_uuid=Column(String,ForeignKey("todos.uuid"),nullable=True,index=True)

    parent=relationship("TodoDB",remote_side=[uuid])