from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List, Optional


from . import Base
from .group import Group
from .associates import student_group_assoc_table


class Student(Base):
    __tablename__ = 'student'
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[Optional[str]]
    firstname: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    address: Mapped[str] = mapped_column(String(50))

    groups: Mapped[List[Group]] = relationship(
        secondary=student_group_assoc_table,
    )