from datetime import datetime

from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author: Mapped[str] = mapped_column(String(60), nullable=False)
    product_name: Mapped[str] = mapped_column(String(60), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    price: Mapped[int] = mapped_column(Integer, default=1)
    min_users: Mapped[int] = mapped_column(Integer, default=1)
    max_users: Mapped[int] = mapped_column(Integer, default=10)

    groups: Mapped[list["Group"]] = relationship("groups", back_populates="product", uselist=True)
    lesson: Mapped["Lesson"] = relationship("lessons", back_populates="product_id", uselist=False)
    customers: Mapped[list["Customer"]] = relationship(
        "customer",
        back_populates="products",
        uselist=True,
        secondary="products_customers",
    )  # many to many


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    group: Mapped["Group"] = relationship("groups", back_populates="student", uselist=False)
    products: Mapped[list["Product"]] = relationship(
        "products",
        back_populates="customers",
        uselist=True,
        secondary="products_customers"
    )  # many to many


class ProductCustomer(Base):
    __tablename__ = "products_customers"

    product_fk: Mapped[list[int]] = mapped_column(ForeignKey("products.id"), primary_key=True)
    customer_fk: Mapped[list[int]] = mapped_column(ForeignKey("customers.customer_id"), primary_key=True)


class Lesson(Base):
    __tablename__ = "lessons"

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), primary_key=True)
    lesson_name: Mapped[str] = mapped_column(String)
    ref_to_video: Mapped[str] = mapped_column(String)

    product: Mapped["Product"] = relationship("products", back_populates="lesson", single_parent=True)


class Group(Base):
    __tablename__ = "groups"

    group_name: Mapped[str] = mapped_column(String, primary_key=True, unique=True)

    product: Mapped["Product"] = relationship("products", back_populates="group", uselist=False)
    student: Mapped[list["Customer"]] = relationship("customers", back_populates="group", uselist=True)
