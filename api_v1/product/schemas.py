from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    author: str
    product_name: str
    start_time: datetime
    price: int
    min_users: int
    max_users: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    author: str | None = None
    product_name: str | None = None
    start_time: datetime | None = None
    price: int | None = None
    min_users: int | None = None
    max_users: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


