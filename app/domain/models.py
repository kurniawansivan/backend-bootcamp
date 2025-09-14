from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Numeric, Text
from app.core.db import Base

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sku: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text(), nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
