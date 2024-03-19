from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProductCustomerAssociation(Base):
    __tablename__ = "product_customer_association"

    product_fk: Mapped[list[int]] = mapped_column(ForeignKey("products.id"), primary_key=True)
    customer_fk: Mapped[list[int]] = mapped_column(ForeignKey("customers.customer_id"), primary_key=True)
