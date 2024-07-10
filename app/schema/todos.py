from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

    class Config:
        from_attributes = True
