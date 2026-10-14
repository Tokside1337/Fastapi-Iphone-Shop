import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, MappedColumn
from backend.app.database import Base
from backend.app.models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = MappedColumn( primary_key=True,index=True)
    username: Mapped[str] = MappedColumn( unique=True)
    email: Mapped[str] = MappedColumn(unique=True)
    hashed_password: Mapped[str] = MappedColumn()
    is_admin: Mapped[bool] = MappedColumn(default=False)


    def __repr__(self):
        return  f"<User(id={self.id}, username='{self.username}')>"