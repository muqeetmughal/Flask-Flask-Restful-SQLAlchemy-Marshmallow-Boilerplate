from application.database import Base
import sqlalchemy as sa
import datetime


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime)
