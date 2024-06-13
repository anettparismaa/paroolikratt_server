from pydantic import BaseModel
from datetime import datetime

class SubmissionBase(BaseModel):
    content: str

    class Config:
        orm_mode = True

class Submission(SubmissionBase):
    content: str
    matched_leak: bool
    matched_generated: bool
    matched_submission: bool

    class Config:
        orm_mode = True

class CreateSubmission(SubmissionBase):
    class Config:
        orm_mode = True

class PasswordBase(BaseModel):
    content: str

    class Config:
        orm_mode = True

class LeakedPassword(PasswordBase):
    content: str

    class Config:
        orm_mode = True

class GeneratedPassword(PasswordBase):
    content: str

    class Config:
        orm_mode = True


class Item(BaseModel):
    value: str
    number: str
    class Config:
        orm_mode = True