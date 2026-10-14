from decimal import Decimal
from sqlalchemy import ForeignKey, func, Numeric, String
from sqlalchemy.orm import relationship, Mapped, MappedColumn
from backend.app.database import Base
from backend.app.models.mixins import TimestampMixin

class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = MappedColumn(primary_key=True, index=True)
    order_id: Mapped[int] = MappedColumn(ForeignKey("orders.id"))
    product_id: Mapped[int] = MappedColumn(ForeignKey("products.id"))

    price_at_purchase: Mapped[Decimal] = MappedColumn(Numeric(10,2))
    quantity: Mapped[int] = MappedColumn(default=1, ge=1)

    order: Mapped[Order] = relationship(back_populates="items")

    def __repr__(self):
        return f"<OrderItem(id={self.id}, Order='{self.order_id}')>"

class Order(Base, TimestampMixin):
    __tablename__ = "orders"

    id: Mapped[int] = MappedColumn(primary_key=True, index=True)
    user_id: Mapped[int] = MappedColumn(ForeignKey("users.id"))

    name: Mapped[str] = MappedColumn(unique=True, index=True)
    total_amount: Mapped[Decimal] = MappedColumn(Numeric(10,2))

    status: Mapped[str] = MappedColumn(String(50),default="Заказ обрабатывается" )
    description: Mapped[str | None]

    items: Mapped[list[OrderItem]] = relationship(back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, name='{self.name}')>"
