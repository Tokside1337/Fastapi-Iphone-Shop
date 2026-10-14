from decimal import Decimal
from sqlalchemy import ForeignKey, func, Numeric
from sqlalchemy.orm import relationship, Mapped, MappedColumn
from backend.app.database import Base
from backend.app.models import Category


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = MappedColumn( primary_key=True,index=True)
    name: Mapped[str] = MappedColumn( unique=True, nullable=False, index = True)
    description: Mapped[str | None]
    price: Mapped[Decimal] = MappedColumn(Numeric(10,2))
    category_id = MappedColumn(ForeignKey("categories.id"),nullable=False)
    image_url: Mapped[str | None]

    category: Mapped["Category"] = relationship(back_populates="products")

    def __repr__(self):
        return  f"<Product(id={self.id}, name='{self.name}')>"