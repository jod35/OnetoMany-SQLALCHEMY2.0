from connect import engine
from models import Base, Program, Course


Base.metadata.create_all(bind=engine)