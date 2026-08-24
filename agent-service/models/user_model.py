from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Relationship,  Column, Integer, Identity

class UserBase(SQLModel):
    email : EmailStr = Field(max_length=256)
    admin : bool = False

class UserModel(UserBase, table=True):
    __tablename__ = 'userstable'

    id : Optional[int] = Field(default=None,sa_column=Column(Integer, Identity(start=1, cycle=False), primary_key=True))
    senha : str = Field(max_length=256) 