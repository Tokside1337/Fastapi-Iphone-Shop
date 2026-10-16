from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.app.database import Base
from backend.app.models.mixins import TimestampMixin

class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    price_at_purchase: Mapped[Decimal] = mapped_column(Numeric(10,2))
    quantity: Mapped[int] = mapped_column(default=1)

    order: Mapped[Order] = relationship(back_populates="items")

    def __repr__(self):
        return f"<OrderItem(id={self.id}, Order='{self.order_id}')>"

class Order(Base, TimestampMixin):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    name: Mapped[str] = mapped_column(unique=True, index=True)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10,2))

    status: Mapped[str] = mapped_column(String(50),default="Заказ обрабатывается" )
    description: Mapped[str | None]

    items: Mapped[list[OrderItem]] = relationship(back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, name='{self.name}')>"
