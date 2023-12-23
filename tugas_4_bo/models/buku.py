from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Buku(Base):
    __tablename__ = "buku"
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    year = Column(Integer)
