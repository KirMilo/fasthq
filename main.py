import datetime

from models.entities import Base, Product

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)  # sql lite  в оперативе.

with Session(engine) as session:
    with session.begin():
        Base.metadata.create_all(engine)
        product1 = Product(
            id=1,
            author="Muzhchina",
            product_name="Muzhskoi product",
            start_time=datetime.datetime(
                year=2024,
                month=4,
                day=5,
                hour=15,
                minute=0,
            ),
            price=100,
            min_users=4,
            max_users=12
        )
        session.add(product1)
    with session.begin():
        result = session.execute(select(Product))
        print(result.scalar())