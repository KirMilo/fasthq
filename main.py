from models import entities

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///memory:", echo=True)

