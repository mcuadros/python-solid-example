from services.sql.connector import Repository
from services.sql.connector import Query


class Company(object):
    name = None

    def __init__(self, name):
        self.name = name


class CompanyQuery(Query):
    def find_by_name(self, name):
        self._filter(Company.name == name)

        return self


class CompanyRepository(Repository):
    _entity_class = Company
    _query_class = CompanyQuery
