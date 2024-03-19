from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .group import Group
    from .lesson import Lesson
    from .customer import Customer


class Product(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author: Mapped[str] = mapped_column(String(60), nullable=False)
    product_name: Mapped[str] = mapped_column(String(60), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    price: Mapped[int] = mapped_column(default=1)
    min_users: Mapped[int] = mapped_column(default=1)
    max_users: Mapped[int] = mapped_column(default=10)

    groups: Mapped[list["Group"]] = relationship(back_populates="product", uselist=True)
    lesson: Mapped["Lesson"] = relationship(back_populates="product", uselist=False)
    customers: Mapped[list["Customer"]] = relationship(
        back_populates="products",
        uselist=True,
        secondary="product_customer_association",
    )  # many to many
