from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from backend.app.schemas.category import CategoryResponse


class _ProductBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

class ProductCreate(_ProductBase):
    name: str
    description: str | None = None
    price: Decimal
    category_id: int
    image_url: str | None = None

class ProductUpdate(_ProductBase):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    category_id: int | None = None
    image_url: str | None = None

class ProductResponse(_ProductBase):
    id: int
    name: str
    description: str | None
    price: Decimal
    category: CategoryResponse

class ProductListResponse(_ProductBase):
    products: list[ProductResponse]
    total: int