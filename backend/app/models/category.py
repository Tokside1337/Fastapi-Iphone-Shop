from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, MappedColumn
from backend.app.database import Base
from backend.app.models import Product


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = MappedColumn(primary_key=True,index=True)
    name: Mapped[str] = MappedColumn(unique=True, index = True)
    slug: Mapped[str] = MappedColumn(unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")

    def __repr__(self):
        return  f"<Category(id={self.id}, name='{self.name}')>"