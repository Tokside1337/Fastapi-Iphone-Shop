from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class _CartBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

class CartItemCreate(_CartBase):
    product_id: int
    quantity: int

class CartItemUpdate(_CartBase):
    product_id: int
    quantity: int

class CartItem(BaseModel):
    product_id: int
    name: str
    price: Decimal
    quantity: int
    subtotal: Decimal
    image_url: str | None

class CartResponse(BaseModel):
    items: list[CartItem]
    total: Decimal
    items_count: int