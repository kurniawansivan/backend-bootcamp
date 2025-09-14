from pydantic import BaseModel, Field

class ProductIn(BaseModel):
    sku: str = Field(min_length=2, max_length=64)
    name: str = Field(min_length=2, max_length=255)
    description: str | None = None
    price: float

class ProductOut(ProductIn):
    id: int
    sku: str
    name: str
    description: str | None
    price: float