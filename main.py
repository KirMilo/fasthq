from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings


# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)  # sql lite  в оперативе.
#
# Base.metadata.create_all(engine)


# with Session(engine) as session:
#     with session.begin():
#         product1 = Product(
#             author="Muzhchina",
#             product_name="Muzhskoi product",
#             start_time=datetime.datetime(
#                 year=2024,
#                 month=4,
#                 day=5,
#                 hour=15,
#                 minute=0,
#             ),
#             price=100,
#             min_users=4,
#             max_users=12
#         )
#         session.add(product1)
#     with session.begin():
#         result = session.execute(select(Product))
#         print(result.scalar().start_time)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server started")
    yield
    print("Server shoot down")


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def main_page():
    return {"message": "Welcome to main page"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
