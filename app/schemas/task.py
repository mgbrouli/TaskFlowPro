from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    user_id: int
    
    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)