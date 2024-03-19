from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .group import Group
    from .product import Product


class Customer(Base):
    customer_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    group_fk: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates="students", uselist=False)
    products: Mapped[list["Product"]] = relationship(
        back_populates="customers",
        uselist=True,
        secondary="product_customer_association"
    )  # many to many
