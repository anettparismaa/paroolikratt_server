from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer,primary_key=True,nullable=False)
    content = Column(String,nullable=False)
    matched_leak = Column(Boolean, server_default='FALSE')
    matched_generated = Column(Boolean, server_default='FALSE')
    matched_submission = Column(Boolean, server_default='FALSE')
    submitted_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class LeakedPassword(Base):
    __tablename__ = "leaked_passwords"
    id = Column(Integer,primary_key=True,nullable=False)
    content = Column(String,nullable=False)

class GeneratedPassword(Base):
    __tablename__ = "generated_passwords"
    id = Column(Integer,primary_key=True,nullable=False)
    content = Column(String,nullable=False)