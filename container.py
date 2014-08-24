from knot import Container
from knot import service

container = Container({
    'db.fqn': 'sqlite:///:memory:',
    'db.echo': False
})


@service(container)
def sqlalchemy_engine(container):
    from sqlalchemy import create_engine

    return create_engine(container['db.fqn'], echo=container['db.echo'])


@service(container)
def sqlalchemy_metadata(container):
    from services.sql import Mapper

    return Mapper().build_metadata()


@service(container)
def sqlalchemy_session(container):
    from sqlalchemy.orm import sessionmaker

    container('sqlalchemy_metadata').create_all(container('sqlalchemy_engine'))
    return sessionmaker(bind=container('sqlalchemy_engine'))()


@service(container)
def models_user_repository(container):
    container('sqlalchemy_session') # quick fix
    from models import UserRepository

    return UserRepository(container('sqlalchemy_session'))


@service(container)
def models_position_repository(container):
    container('sqlalchemy_session') # quick fix
    from models.position import PositionRepository

    return PositionRepository(container('sqlalchemy_session'))


@service(container)
def models_company_repository(container):
    container('sqlalchemy_session') # quick fix
    from models import CompanyRepository

    return CompanyRepository(container('sqlalchemy_session'))


