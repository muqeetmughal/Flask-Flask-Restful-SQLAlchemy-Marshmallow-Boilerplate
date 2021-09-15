from application.extensions import marshmallow


class BaseResource(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        include_fk = True
        load_only = ('password',)
        dump_only = ('id',)
