from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import Product, db_helper
from .dependencies import product_by_id
from .schemas import ProductCreate, ProductUpdate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scopped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
        product: Product = Depends(product_by_id),
):
    return product


@router.put("/{product_id}/")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_product(session=session, product=product)