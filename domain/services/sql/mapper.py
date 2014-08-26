from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
import domain.models as models


class Mapper(object):
    _metadata = None

    def build_metadata(self):
        self._create_metadata()
        self._configure_metadata()

        return self._metadata

    def _create_metadata(self):
        self._metadata = MetaData()

    def _configure_metadata(self):
        mapper(models.User, Table(
            'users',
            self._metadata,
            Column('id', Integer, primary_key=True),
            Column('email', String),
            Column('status', String),
            Column('first_name', String(50)),
            Column('last_name', String(50)),
            Column('created_at', Integer),
            Column('salt', String(50)),
            Column('password', String(255)),
        ))

        mapper(models.Company, Table(
            'companies',
            self._metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50))
        ))

        association_table = Table(
            'users_positions',
            self._metadata,
            Column('user_id', Integer, ForeignKey('users.id')),
            Column('position_id', Integer, ForeignKey('positions.id'))
        )

        mapper(models.Position, Table(
            'positions',
            self._metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String(50)),
            Column('company_id', Integer, ForeignKey("companies.id")),
        ), properties={
            'company': relationship(models.Company),
            'candidates': relationship(
                models.User,
                secondary=association_table
            )
        })
