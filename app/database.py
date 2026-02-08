from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# engine = create_engine(DATABASE_URL)

# engine = create_engine(
#     settings.database_url,
#     connect_args={"sslmode": "require"} if "render.com" in settings.database_url else {}
# )

CLOUD_DB_KEYS = ["render"]

use_ssl = any(key in settings.database_url for key in CLOUD_DB_KEYS)

engine = create_engine(
    settings.database_url,
    connect_args={"sslmode": "require"} if use_ssl else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()