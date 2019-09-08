def processData():
	data = open('countries.txt','r').read().split('\n')
	capitals = { }
	for i in data:
		tmp = i.split(',')
		capitals[tmp[0]] = tmp[1]

	return capitals
