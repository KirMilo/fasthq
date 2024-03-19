from typing import Annotated

from fastapi.params import Path
from sqlalchemy.ext.asyncio import AsyncSession


async def product_by_id(
        product_id: Annotated[int, Path],
        session: AsyncSession
):
    pass
