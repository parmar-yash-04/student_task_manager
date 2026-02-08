from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from .config import test_settings

engine = create_engine(test_settings.database_url)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)