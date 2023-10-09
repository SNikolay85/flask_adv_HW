from typing import Optional

from pydantic import BaseModel


class CreateAdv(BaseModel):
    header: str
    description: str
    user: str


class UpdateAdv(BaseModel):
    header: Optional[str]
    description: Optional[str]
    user: str
