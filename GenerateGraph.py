from random import randint, randrange


def checkValidity(graph):
	"""
	Check if a graph is valid
	"""
	for key in graph:
			for valKey in graph[key]:
					if(valKey not in graph.keys()):
							return False
	return True


keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generateGraph():
	"""
	Generate a graph using keys above
	"""
	random_last_key_index = randint(1, len(keys))
	graph = {}

	for i in range(0, random_last_key_index):
			graph[keys[i]] = {}
			random_size = randint(1, random_last_key_index)
			for j in range(random_size):
					random_key_index = randint(0, random_size - 1)
					if(random_key_index == i):
							continue
					graph[keys[i]][keys[random_key_index]] = randint(0, 10)

	return graph
