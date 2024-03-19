from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product
    from .customer import Customer


class Group(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    group_name: Mapped[str] = mapped_column()

    product_fk: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="groups", uselist=False)

    students: Mapped[list["Customer"]] = relationship(back_populates="group", uselist=True)
