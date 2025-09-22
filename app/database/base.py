# import
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import DateTime
from datetime import datetime


# define base
class Base(DeclarativeBase):
    pass


# declaring basemodel
class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
