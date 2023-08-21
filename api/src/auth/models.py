from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from database import Base, metadata


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
