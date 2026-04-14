from pydantic import BaseModel

class ChatRequest(BaseModel):
    input: str

class ChatResponse(BaseModel):
    response: str

class APIResponse(BaseModel):
    message: str
    status_code: int
    response: ChatResponse | None=None
    error: str | None=None