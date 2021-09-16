from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from application.database import db_session


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        include_fk = True
        load_only = ('password',)
        dump_only = ('id',)
        load_instance = True
        sqla_session = db_session
