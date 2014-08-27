from knot import service


def apply_to_container(container):
    @service(container)
    def sqlalchemy_engine(container):
        from sqlalchemy import create_engine

        return create_engine(container['db.fqn'], echo=container['db.echo'])

    @service(container)
    def sqlalchemy_metadata(container):
        import domain.services.sql.mapper as sql

        return sql.Mapper().build_metadata()

    @service(container)
    def sqlalchemy_session(container):
        from sqlalchemy.orm import sessionmaker

        container('sqlalchemy_metadata').\
            create_all(container('sqlalchemy_engine'))

        return sessionmaker(bind=container('sqlalchemy_engine'))()

    @service(container)
    def models_user_repository(container):
        import domain.models as models

        return models.UserRepository(container('sqlalchemy_session'))

    @service(container)
    def models_position_repository(container):
        import domain.models as models

        return models.PositionRepository(container('sqlalchemy_session'))

    @service(container)
    def models_company_repository(container):
        import domain.models as models

        session = container('sqlalchemy_session')
        return models.company.CompanyRepository(session)
