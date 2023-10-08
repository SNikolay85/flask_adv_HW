from typing import Optional

from pydantic import BaseModel, validator


class CreateAdv(BaseModel):
    header: str
    description: str
    user: str


    # @validator("password")
    # def secure_password(cls, value):
    #     if len(value) <= 8:
    #         raise ValueError("Password is short")
    #     return value


class UpdateAdv(BaseModel):
    header: Optional[str]
    description: Optional[str]
    user: Optional[str]

    @validator('user')
    def exist_user(cls, value):
        for key, val in if value not in
    # @validator("password")
    # def secure_password(cls, value):
    #     if len(value) <= 8:
    #         raise ValueError("Password is short")
    #     return value
