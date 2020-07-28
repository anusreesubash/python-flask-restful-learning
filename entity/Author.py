authors = [{
	'id': 1,
	'name':'anusree',
	'email':'anusreesubash@gmail.com'
}]

id = 2;

def findAuthorById(id):
	global authors
	return next((x for x in authors if x['id'] == int(id)), None)

class Author():
	def all():
		return authors

	def create(name, email):
		global id
		author = {
			'id': id,
			'name': name,
			'email': email
		}
		authors.append(author)
		id = id+1
		return author

	def getById(id):
		for author in authors:
			if author['id'] == int(id):
				return author

		return ({'message': 'author not found'})

	def deleteById(id):
		global authors
		author = findAuthorById(id)
		if author == None:
			return({'message':'author not found'})
		authors = list(filter(lambda x: x['id'] != int(id), authors))
		return ({'message': 'author removed'})

	def updateById(id, name, email):
		author = findAuthorById(id)
		if author == None:
			return({'message':'author not found'})
		author['name'] = name
		author['email'] = email
		return author