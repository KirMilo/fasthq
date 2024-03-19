from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.params import Path
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper


async def product_by_id(
        product_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found"
    )