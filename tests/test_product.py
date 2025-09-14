from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_list_detail_products():
    # create
    r = client.post("/products", json={
        "sku": "BRACE-001",
        "name": "Rose Quartz Bracelet",
        "description": "Pink stone",
        "price": 49.9
    })
    assert r.status_code == 201, r.text
    pid = r.json()["id"]

    # list + search
    r2 = client.get("/products?q=Quartz&limit=5&offset=0")
    assert r2.status_code == 200
    ids = [p["id"] for p in r2.json()]
    assert pid in ids

    # detail
    r3 = client.get(f"/products/{pid}")
    assert r3.status_code == 200
    body = r3.json()
    assert body["sku"] == "BRACE-001"
    assert body["name"] == "Rose Quartz Bracelet"
