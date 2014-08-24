from services.sql.connector import Repository
from services.sql.connector import Query


class Position(object):
    company = None
    candidates = []
    title = None

    def __init__(self, title, company):
        self.company = company
        self.title = title


class PositionQuery(Query):
    def find_by_company(self, company):
        self._filter(Position.company == company)

        return self


class PositionRepository(Repository):
    _entity_class = Position
    _query_class = PositionQuery
