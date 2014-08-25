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
    import example.services.sql.mapper as sql

    return sql.Mapper().build_metadata()


@service(container)
def sqlalchemy_session(container):
    from sqlalchemy.orm import sessionmaker

    container('sqlalchemy_metadata').create_all(container('sqlalchemy_engine'))
    return sessionmaker(bind=container('sqlalchemy_engine'))()


@service(container)
def models_user_repository(container):
    import example.models as models

    return models.UserRepository(container('sqlalchemy_session'))


@service(container)
def models_position_repository(container):
    import example.models as models

    return models.PositionRepository(container('sqlalchemy_session'))


@service(container)
def models_company_repository(container):
    import example.models as models

    return models.company.CompanyRepository(container('sqlalchemy_session'))


