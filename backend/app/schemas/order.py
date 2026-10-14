import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class _OrderBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

class OrderItemCreate(_OrderBase):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderItemResponse(_OrderBase):
    id:int
    product_id: int
    quantity: int = Field(..., gt=0)
    price: Decimal

    @property
    def total_item_price(self) -> Decimal:
        return self.price * self.quantity

class OrderCreate(_OrderBase):
    status: str
    items: list[OrderItemResponse] = Field(..., min_length=1)

class OrderUpdate(_OrderBase):
    status: str

class OrderResponse(_OrderBase):
    id: int
    user_id: int
    items: list[OrderItemResponse]
    total_price: Decimal
    created_at: datetime.datetime
    updated_at: datetime.datetime