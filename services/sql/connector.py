class Repository(object):
    _entity_class = None
    _query_class = None

    __session = None

    def __new__(cls, *args, **kwargs):
        if cls is Repository:
            raise TypeError("Repository class cannot be instantiated")

        return object.__new__(cls, *args, **kwargs)

    def __init__(self, session):
        self.__session = session

    def new(self, *args, **kwargs):
        return self._entity_class(*args, **kwargs)

    def insert(self, entity):
        self.__session.add(entity)
        self.__session.commit()

    def delete(self, entity):
        self.__session.delete(entity)

    def commit(self):
        self.__session.commit()

    def find(self, query):
        return Result(query.sql_query)

    def create_query(self):
        return self._query_class(self.__session.query(self._entity_class))


class Query(object):
    sql_query = None

    def __new__(cls, *args, **kwargs):
        if cls is Query:
            raise TypeError("Query class cannot be instantiated")

        return object.__new__(cls, *args, **kwargs)

    def __init__(self, sql_query):
        self.sql_query = sql_query

    def _filter(self, *condition):
        self.sql_query = self.sql_query.filter(*condition)


class Result(object):
    __sql_query = None

    def __init__(self, sql_query):
        self.__sql_query = sql_query

    def all(self):
        return self.__sql_query.all()

    def one(self):
        return self.__sql_query.one()

    def count(self):
        pass
