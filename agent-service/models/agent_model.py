from typing import Optional
from sqlmodel import Field, SQLModel, Relationship,  Column, Integer, Identity

class AgentResponseBase(SQLModel):
    perguntas : str = Field(max_length=256)

class AgentModel(AgentResponseBase, table=True):
    __tablename__ = 'agentresponses'
    
    id : Optional[int] = Field(default=None, sa_column=Column(Integer, Identity(start=1, cycle=False), primary_key=True))