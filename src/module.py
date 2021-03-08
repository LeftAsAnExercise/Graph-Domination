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
	
def NodeAdd(SolutionVector):
    solutionVector[proportional_probability(solutionVector)] = 1

    return
	
def getNodes(d):
    


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
		
def MainLoop(initTemp, finalTemp, CoolingRatio, EpochLength, initSolutionVector):
	XBest = initSolutionVector
	k = 0
	currentTemp=initTemp
	while currentTemp > finalTemp : 
		for M in range(1,EpochLength+1):
		
	return 