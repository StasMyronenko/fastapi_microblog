from core.db import Base

from user.models import User

from sqlalchemy import Integer, Column, DateTime, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'microblog_post'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text(350))
    date = Column(DateTime)

    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)

