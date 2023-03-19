import datetime
from sqlalchemy import orm, Column, Integer, String, Date
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    modified_date = Column(Date, default=datetime.datetime.today().date())

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
