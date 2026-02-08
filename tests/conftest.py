import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from tests.database import TestingSessionLocal, engine
from app.models import Base

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture()
def client():
    return TestClient(app)