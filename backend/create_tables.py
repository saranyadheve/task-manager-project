from database import engine
from models import Base

# This will create tables if they do not exist
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
