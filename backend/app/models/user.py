from sqlalchemy.orm import Mapped, mapped_column
from backend.app.database import Base
from backend.app.models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column( primary_key=True,index=True)
    username: Mapped[str] = mapped_column( unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(default=False)


    def __repr__(self):
        return  f"<User(id={self.id}, username='{self.username}')>"