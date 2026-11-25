from app.database import Base, engine
import app.models  # noqa: F401  (loads the models so Base knows them)

Base.metadata.create_all(engine)
print("tables created")