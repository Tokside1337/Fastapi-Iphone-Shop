from pydantic import BaseModel, ConfigDict, EmailStr


class _UserBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

class UserCreate(_UserBase):
    username: str
    email: EmailStr
    hashed_password: str
    is_admin: bool = False

class UserUpdate(_UserBase):
    username: str | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None
    is_admin: bool | None = None

class UserResponse(_UserBase):
    id: int
    username: str
    email: EmailStr
