import domain.services.sql.connector as connector


class Company(object):
    name = None

    def __init__(self, name):
        self.name = name


class CompanyQuery(connector.Query):
    def find_by_name(self, name):
        self._filter(Company.name == name)

        return self


class CompanyRepository(connector.Repository):
    _entity_class = Company
    _query_class = CompanyQuery
