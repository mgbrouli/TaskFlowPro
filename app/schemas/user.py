from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    
class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    
    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)
    
class Token(BaseModel):
    access_token: str
    token_type: str