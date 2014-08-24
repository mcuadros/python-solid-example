from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.sql import Mapper
from models import UserRepository

# bootstrap
engine = create_engine('sqlite:///:memory:', echo=False)
metadata = Mapper().build_metadata()
metadata.create_all(engine)
session = sessionmaker(bind=engine)()


# examples
user_repository = UserRepository(session)

# insert
user = user_repository.new(email='maximo@tyba.com')
user.first_name = 'Maximo'
user.password = '123456'
user_repository.insert(user)
print 'User created with id %d' % user.id
session.refresh(user)


# find
query = user_repository.create_query().\
    find_by_email('maximo@tyba.com').\
    find_active()

found = user_repository.find(query).one()
print 'User %s was created at %s' % (found.email, found.created_at)

# delete
user_repository.delete(found)
found = user_repository.find(query).all()
if len(found) == 0:
    print 'Deleted success!'

