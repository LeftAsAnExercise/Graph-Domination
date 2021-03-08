class GraphTools:
	def createMovementDictionary(length, func=GraphTools.knight):
		graphDictionary = []
		for i in range(len(solutionVector)):
			graphDictionary = func(i, length)
		return graphDictionary

	def knight(i, length):
		output = []
		x = i % length
		y = i // length
		if x - 1 >= 0 and y - 2 >= 0:
			output.append(x + y * length)
		if x - 1 >= 0 and y + 2 < length:
			output.append(x + y * length)
		if x - 2 >= 0 and y - 1 >= 0:
			output.append(x + y * length)
		if x - 2 >= 0 and y + 1 < length:
			output.append(x + y * length)
		if x + 2 < length and y - 1 >= 0:
			output.append(x + y * length)
		if x + 2 < length and y + 1 < length:
			output.append(x + y * length)
		if x + 1 < length and y - 2 >= 0:
			output.append(x + y * length)
		if x + 1 < length and y + 2 >= 0:
			output.append(x + y * length)
		return output

	def bishop(i, length):
		output = []
		x = i % length
		y = i // length
		for j in range(length):
			if x + j < length and y + j < length:
				output.append((j + x) + (y + j) * length)
			if x + j < length and y - j >= 0:
				output.append((j + x) + (y - j) * length)
			if x - j >= - and y - j >= 0:
				output.append((j - x) + (y - j) * length)
			if x - j >= - and y + j < length:
				output.append((j - x) + (y + j) * length)
		return output
			


class SimulatedAnnealing:
	def getNodes(d):
		nodes = []
		for i in d.keys():
			if i not in nodes:
				nodes.append(i)
			for j in d[i]:
				if j not in nodes:
					nodes.append(j)

		return len(nodes)

	def calculateObjectiveFunction(length, graphDictionary, solutionVector):
		d = dict()
		for i in range(len(solutionVector)):
			if solutionVector[i]:
				d[i] = graphDictionary[i]
		V = length ** 2
		n = getNodes(d)
		G = solutionVector.count(1)
		return n/V + 1/(V*G)