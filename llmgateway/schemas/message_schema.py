from pydantic import BaseModel

class MessageSchema(BaseModel):
    role : str # Message's Author ex: user
    content : str

    


    