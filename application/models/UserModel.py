from application.helper.base.Model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy as sa


class User(BaseModel):
    __tablename__ = "users"

    first_name = sa.Column(sa.String(25), nullable=False)
    last_name = sa.Column(sa.String(25))
    username = sa.Column(sa.String(50), unique=True)
    email = sa.Column(sa.String(100))
    gender = sa.Column(sa.Enum('male', 'female'))
    password = sa.Column(sa.String(255))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
