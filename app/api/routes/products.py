from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.api.schemas import ProductIn, ProductOut
from app.domain.models import Product

router = APIRouter(prefix="/products", tags=["products"])

@router.post("", response_model=ProductOut, status_code=201)
def create_product(data: ProductIn, db: Session = Depends(get_db)):
    if db.query(Product).filter(Product.sku == data.sku).first():
        raise HTTPException(409, detail="SKU already exists")
    p = Product(**data.model_dump())
    db.add(p); db.commit(); db.refresh(p)
    return ProductOut(id=p.id, sku=p.sku, name=p.name, description=p.description, price=float(p.price))

@router.get("", response_model=list[ProductOut])
def list_products(
    q: str | None = None,
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Product)
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(Product.name.ilike(like))
    rows = query.order_by(Product.id.desc()).limit(limit).offset(offset).all()
    return [ProductOut(id=r.id, sku=r.sku, name=r.name, description=r.description, price=float(r.price)) for r in rows]

@router.get("/{pid}", response_model=ProductOut)
def get_product(pid: int, db: Session = Depends(get_db)):
    p = db.get(Product, pid)
    if not p:
        raise HTTPException(404, detail="Product not found")
    return ProductOut(id=p.id, sku=p.sku, name=p.name, description=p.description, price=float(p.price))
