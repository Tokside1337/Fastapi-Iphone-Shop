from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from backend.app.models import Category


class _CategoryBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

class CategoryCreate(_CategoryBase):
    name: str


class CategoryResponse(_CategoryBase):
    id: int
    name: str
    slug: str
