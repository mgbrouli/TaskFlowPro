from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./taskflow.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

sesisonLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = sesisonLocal()
    try:
        yield db
    finally:
        db.close()