def knight(i, length):
	output = []
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	if x - 1 >= 0 and y - 2 >= 0:
		output.append((x - 1) + (y - 2) * l)
	if x - 1 >= 0 and y + 2 < l:
		output.append((x - 1) + (y + 2) * l)
	if x - 2 >= 0 and y - 1 >= 0:
		output.append((x - 2) + (y - 1) * l)
	if x - 2 >= 0 and y + 1 < l:
		output.append((x - 2) + (y + 1) * l)
	if x + 2 < l and y - 1 >= 0:
		output.append((x + 2) + (y - 1) * l)
	if x + 2 < l and y + 1 < length:
		output.append((x - 2) + (y + 1) * l)
	if x + 1 < l and y - 2 >= 0:
		output.append((x + 1) + (y - 2) * l)
	if x + 1 < l and y + 2 < length:
		output.append((x + 1) + (y + 2) * l)
	return output

def bishop(i, length):
	output = []
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	for j in range(l):
		if x + j < l and y + j < l:
			output.append((x + j) + (y + j) * l)
		if x + j < l and y - j >= 0:
			output.append((j + x) + (y - j) * l)
		if x - j >= 0 and y - j >= 0:
			output.append((j - x) + (y - j) * l)
		if x - j >= 0 and y + j < l:
			output.append((j - x) + (y + j) * l)
	return output

def rook(i, length):
	output = []
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	for j in range(l):
		if x + j < l:
			output.append((j + x) + (y) * l)
		if x - j >= 0:
			output.append((x - j) + (y) * l)
		if y + j < l:
			output.append((x) + (y + j) * l)
		if y - j >= 0:
			output.append((x) + (y - j) * l)
	return output

def pawn(i, length):
	return diagonal(i, length, limit=[1, 1, 0, 0])

def orthogonal(i, length, limit=[1, 1, 1, 1]):
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	if len(limit) < 4:
		limit = limit + [0] * (4 - len(limit))
	if x + limit[0] < l and limit[0] > 0:
		output.append((x + limit[0]) + (y) * l)
	if y + limit[1] < l and limit[1] > 0:
		output.append((x) + (y + limit[1]) * l)
	if x - limit[2] >= 0 and limit[2] > 0:
		output.append((x - limit[2]) + (y) * l)
	if y - limit[3] >= 0 and limit[3] > 0:
		output.append((x) + (y - limit[3]) * l)
	return output

def diagonal(i, length, limit=[1, 1, 1, 1]):
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	if len(limit) < 4:
		limit = limit + [0] * (4 - len(limit))
	if x + limit[0] < l and y + limit[0] < l and limit[0] > 0:
		output.append((x + limit[0]) + (y + limit[0]) * l)
	if x - limit[1] >= 0 and y + limit[1] and limit[1] > 0:
		output.append((x - limit[1]) + (y + limit[1]) * l)
	if x - limit[2] >= 0 and y - limit[2]>= 0 and limit[2] > 0:
		output.append((x - limit[2]) + (y - limit[2]) * l)
	if x + limit[3] >= 0 y - limit[3] >= 0 and limit[3] > 0:
		output.append((x) + (y - limit[3]) * l)
	return output

def hippogonal(i, length, limit=[1, 4]):
	output = []
	x = i % length
	y = i // length
	l = length ** (1 / 2)
	try:
		a = limit[0]
		b = limit[1]
	except IndexError:
		return None
	if x - a >= 0 and y - b >= 0:
		output.append((x - a) + (y - b) * l)
	if x - a >= 0 and y + b < l:
		output.append((x - a) + (y + b) * l)
	if x - b >= 0 and y - a >= 0:
		output.append((x - b) + (y - a) * l)
	if x - b >= 0 and y + a < l:
		output.append((x - b) + (y + a) * l)
	if x + b < l and y - a >= 0:
		output.append((x + b) + (y - a) * l)
	if x + b < l and y + a < length:
		output.append((x - b) + (y + a) * l)
	if x + a < l and y - b >= 0:
		output.append((x + a) + (y - b) * l)
	if x + a < l and y + b < length:
		output.append((x + a) + (y + b) * l)
	return output

def queen(i, length):
	output = []
	output1 = bishop(i, length)
	output2 = rook(i, length)
	return list(set(output1 + output2))

def createFairNotation(string):
	def fair(i, length):
		output = []
		if string.contains("n+"):
			output += rook(i, length)
		if string.contains("+")
			output += orthogonal(i, length, n=n)
		return list(set(output))
	return fair

def createMovementDictionary(length, func=knight):
	graphDictionary = dict()
	for i in range(len(solutionVector)):
		graphDictionary[i] = func(i, length)
	return graphDictionary