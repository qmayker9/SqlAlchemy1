from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List

from . import Base
from .group import Group
from .associates import lesson_group_assoc_table



class Lesson(Base):
    __tablename__ = 'lessons'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    groups: Mapped[List[Group]] = relationship(secondary=lesson_group_assoc_table)