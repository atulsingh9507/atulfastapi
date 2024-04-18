from pydantic import BaseModel, Field
from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class ShowUserBase(UserBase):
    blogs: List[ShowBlog] = []

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password:str
    

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Blog(BlogBase):
    id: int
    creator_id: int

    class Config:
        orm_mode = True

class ShowUser(ShowUserBase):

    pass



class User(BaseModel):
    name: str
    email: str
    password: str    
class Login(BaseModel):
    username: str
    password: str