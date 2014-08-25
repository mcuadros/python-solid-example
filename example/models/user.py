import datetime
import bcrypt

import example.services.sql.connector as connector


class User(object):
    id = None
    email = None
    status = None
    first_name = None
    last_name = None
    created_at = None
    password = None
    salt = None

    def __init__(self, email):
        self.email = email
        self.created_at = datetime.datetime.now()
        self.status = 'active'

    @property
    def password(self):
        return self.__dict__.get('password')

    @password.setter
    def password(self, plain_password):
        self.salt = bcrypt.gensalt()
        self.__dict__['password'] = bcrypt.hashpw(plain_password, self.salt)


class UserQuery(connector.Query):
    def find_by_email(self, email):
        self._filter(User.email == email)

        return self

    def find_active(self):
        self._filter(User.status == 'active')

        return self


class UserRepository(connector.Repository):
    _entity_class = User
    _query_class = UserQuery
