from flask_restful import Resource
from application.database import db_session
from flask_restful import abort
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from flask import request

class BaseResource(Resource):
    def load_model_object(self, schema):
        try:
            request_data = request.get_json()
            if request_data:
                return schema.load(request_data)
            else:
                abort(404, response={
                    'message': 'Something Wrong in Base Resource'
                })
        except ValidationError as err:
            self.abort(400, err.normalized_messages())

    def find(self, model, **kwargs):
        record = model.query.filter_by(**kwargs).first()
        return record

    def abort(self, http_status, message=None):

        if message:
            abort(http_status, response={
                'message': message
            })

        abort(http_status, response={
            'message': "Something Went Wrong."
        })

    def list_exist_or_404(self, model_query, schema):
        if model_query:
            return schema.dump(model_query, many=True), 200
        abort(404, response={
            'message': 'Nothing Found'
        })

    def single_exist_or_404(self, model_query, schema):
        if model_query:
            return schema.dump(model_query), 200
        abort(404, response={
            'message': 'Nothing Found'
        })

    def bulk_save(self, list_of_records, commit=True):
        # self.before_save()
        db_session.add_all(list_of_records)
        # db.session.add(self)
        if commit:
            try:
                try:
                    db_session.commit()
                except IntegrityError as err:
                    self.abort(400, str(err))
            except Exception as e:
                db_session.rollback()
                raise e
