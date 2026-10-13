from pydantic import BaseModel
from __all_schemas import MessageSchema

class ChatRequestSchema(BaseModel):
    messages : list[MessageSchema]
