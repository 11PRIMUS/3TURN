from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base=declarative_base()

class gen_record(Base):
    __tablename__="generations"

    id=Column(String, primary_key=True)
    user_id=Column(String, index=True)
    prompt=Column(Text)
    created_at=Column(DateTime, default=datetime.utcnow)
    