from application.database import db_session
from sqlalchemy.exc import IntegrityError
import datetime
from flask_restful import abort
import sqlalchemy as sa

from werkzeug.security import check_password_hash


class TimeStampMixin:
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime)


class CrudModelMixin:

    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def save(self, commit=True):
        # self.before_save()
        db_session.add(self)
        # db.session.add(self)
        if commit:
            try:
                try:
                    db_session.commit()
                except IntegrityError as err:
                    db_session.rollback()
                    self.abort(400, str(err.orig))
            except IntegrityError as err:
                db_session.rollback()
                self.abort(400, str(err.orig))
        # self.after_save()

    def before_update(self, *args, **kwargs):
        pass

    def after_update(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.before_update(*args, **kwargs)
        db_session.commit()
        self.after_update(*args, **kwargs)

    def delete(self, commit=True, soft_delete=False):

        if not self.deleted_at:
            if commit:
                if soft_delete:
                    try:
                        self.deleted_at = datetime.datetime.utcnow()
                        db_session.commit()
                        print(self, 'Soft deleted')
                    except IntegrityError as e:
                        db_session.rollback()
                        self.abort(409, "Integrity Error, Cant Delete Because this Item")
                    except Exception as e:
                        db_session.rollback()
                        raise e
                else:
                    db_session.delete(self)
                    try:
                        db_session.commit()
                        print(self, 'deleted')
                    except IntegrityError as e:
                        db_session.rollback()
                        self.abort(409, "Integrity Error, Cant Delete this Item")
                    except Exception as e:
                        db_session.rollback()
                        raise e
        else:
            abort(404, response={
                "message": "Already Deleted"
            })

    @classmethod
    def find(cls, **kwargs):
        if kwargs:
            return db_session.query(cls).filter_by(**kwargs).first()
        return abort(400, response={
            "message": "Id or keyword argument missing following /"
        })

    @classmethod
    def findAll(cls, **kwargs):

        if kwargs:
            return db_session.query(cls).filter_by(**kwargs).all()
        else:
            return db_session.query(cls).all()

    def abort(self, http_status, message=None):

        if message:
            abort(http_status, response={
                'message': message
            })

        abort(http_status, response={
            'message': "Something Went Wrong."
        })

    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)


class CrudTimeStampModelMixin(CrudModelMixin, TimeStampMixin):
    pass
