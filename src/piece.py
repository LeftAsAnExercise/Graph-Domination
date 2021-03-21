def knight(i, length):
	output = []
	x = i % length
	y = i // length
	if x - 1 >= 0 and y - 2 >= 0:
		output.append([x - 1, y - 2])
	if x - 1 >= 0 and y + 2 < length:
		output.append([x - 1, y + 2])
	if x - 2 >= 0 and y - 1 >= 0:
		output.append([x - 2, y - 1])
	if x - 2 >= 0 and y + 1 < length:
		output.append([x - 2, y + 1])
	if x + 2 < length and y - 1 >= 0:
		output.append([x + 2, y +- 1])
	if x + 2 < length and y + 1 < length:
		output.append([x + 2, y + 1])
	if x + 1 < length and y - 2 >= 0:
		output.append([x + 1, y - 2])
	if x + 1 < length and y + 2 >= 0:
		output.append([x + 1, y + 2])
	return output

def bishop(i, length):
	output = []
	x = i % length
	y = i // length
	for j in range(length):
		if x + j < length and y + j < length:
			output.append([(j + x), (y + j)])
		if x + j < length and y - j >= 0:
			output.append([(j + x), (y - j)])
		if x - j >= - and y - j >= 0:
			output.append([(j - x),(y - j)])
		if x - j >= - and y + j < length:
			output.append([(j - x), (y + j)])
	return output

def rook(i, length):
	output = []
	x = i % length
	y = i // length
	for j in range(length):
		if x + j < length:
			output.append([(j + x), (y)])
		if x - j >= 0:
			output.append([(x - j), (y)])
		if y + j < length:
			output.append([(x),(y + j)])
		if y - j >= 0:
			output.append([(x), (y - j)])
	return output

def orthogonal(i, length, limit=1):
	x = i % length
	y = i // length
	if x + j < length:
		output.append([(limit + x), (y)])
	if x - j >= 0:
		output.append([(x - limit), (y)])
	if y + j < length:
		output.append([(x),(y + limit)])
	if y - j >= 0:
		output.append([(x), (y - limit)])
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
	graphDictionary = []
	for i in range(len(solutionVector)):
		graphDictionary += func(i, length)
	return graphDictionary