from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column( primary_key=True,index=True)
    name: Mapped[str] = mapped_column( unique=True, nullable=False, index = True)
    description: Mapped[str | None]
    price: Mapped[Decimal] = mapped_column(Numeric(10,2))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"),nullable=False)
    image_url: Mapped[str | None]

    category: Mapped["Category"] = relationship(back_populates="products")

    def __repr__(self):
        return  f"<Product(id={self.id}, name='{self.name}')>"