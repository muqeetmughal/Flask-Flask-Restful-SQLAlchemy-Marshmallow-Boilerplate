from application.database import Base
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
import datetime
from flask_restful import abort
from application.database import db_session


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = sa.Column(sa.DateTime)

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
                    self.abort(400, str(err))
            except Exception as e:
                db_session.rollback()
                raise e
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
