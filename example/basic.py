from example.container import container

# examples
user_repository = container('models_user_repository')

## Plain case
# insert
user = user_repository.new(email='maximo@tyba.com')
user.first_name = 'Maximo'
user.password = '123456'
user_repository.insert(user)
print 'User created with id %d' % user.id


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

## Relational case
company_repository = container('models_company_repository')
position_repository = container('models_position_repository')

# insert
company = company_repository.new(name='Tyba')
position = position_repository.new(title='Superb job', company=company)

users = (
    user_repository.new(email='maximo@tyba.com'),
    user_repository.new(email='miguel@tyba.com')
)

[position.candidates.append(u) for u in users]

position_repository.insert(position)

# find
query = position_repository.create_query().find_by_company(company)
found = position_repository.find(query).one()

print 'Position: %s @ %s, Candidate(s): %d' % (
    found.title,
    found.company.name,
    len(found.candidates)
)

for candidate in found.candidates:
    print '\tCandidate %s' % candidate.email
