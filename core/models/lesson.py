from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base


if TYPE_CHECKING:
    from .product import Product


class Lesson(Base):
    lesson_name: Mapped[str] = mapped_column(primary_key=True, unique=True)
    ref_to_video: Mapped[str] = mapped_column()

    product_fk: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="lesson", single_parent=True)
