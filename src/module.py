from random import choice, uniform
from numpy import array, where

def calculateObjectiveFunction(length, graphDictionary, solutionVector):
    d = dict()
	for i in range(len(solutionVector)):
		if solutionVector[i]:
			d[i] = graphDictionary[i]
	V = length ** 2
	n = getNodes(d)
	G = solutionVector.count(1)
	return n/V + 1/(V*G)

def stochastic_local_search(solutionVector):
    print(calculateObjectiveFunction(solutionVector))
    while True:
        objective_function = calculateObjectiveFunction(solutionVector)
        if(objective_function >= 1):
            solutionVector[inverse_probability(solutionVector)] = 0
        else:
            solutionVector[proportional_probability(solutionVector)] = 1
        if calculateObjectiveFunction(solutionVector) < objective_function:
            i1 = int(choice(array(where(array(solutionVector) == 0)).T))
            i2 = int(choice(array(where(array(solutionVector) == 1)).T))
            solutionVector[i1], solutionVector[i2] = solutionVector[i2], solutionVector[i1]
        if(calculateObjectiveFunction(solutionVector) <= objective_function):
            break
    return solutionVector       
    
  
def proportional_probability(solutionVector):
    l = []
    for index, value in enumerate(solutionVector):
        if not value:
            l.extend([index] * len(graphDictionary[index]))
    return choice(l)
	
def inverse_probability(solutionVector):
    d = {}
    s = 0
    for index, value in enumerate(solutionVector):
        if value:
            s += 1/len(graphDictionary[index])
            d[s] = index
    p = uniform(0,s)
    for i in d.keys():
        if p <= i:
            return d[i]

def NodeReduction(solutionVector):
    solutionVector[inverse_probability(solutionVector)] = 0
	return	
def NodeAdd(SolutionVector):
    solutionVector[proportional_probability(solutionVector)] = 1
    return
def NodeSwapper(solutionVector):
    i1 = int(choice(array(where(array(solutionVector) == 0)).T))
    i2 = int(choice(array(where(array(solutionVector) == 1)).T))
    solutionVector[i1], solutionVector[i2] = solutionVector[i2], solutionVector[i1]
	return
def getNodes(d):
    nodes = []
    for i in d.keys():
        if i not in nodes:
            nodes.append(i)
        for j in d[i]:
            if j not in nodes:
                nodes.append(j)

    return len(nodes)

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

def MainLoop(initTemp, finalTemp, CoolingRatio, EpochLength, initSolutionVector):
	XBest = initSolutionVector
	k = 0
	currentTemp=initTemp
	while currentTemp > finalTemp : 
		for M in range(1,EpochLength+1):
		
	return 