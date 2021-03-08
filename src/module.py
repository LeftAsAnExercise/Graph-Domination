##Comment
from random import choice, uniform
from numpy import array, where

class GraphTools:
   def 
class SimulatedAnnealing:
   def NodeSwap(SolutionVector):
    	   
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

def calculateObjectiveFunction(length, graphDictionary, solutionVector):
	d = dict()
	for i in range(len(solutionVector)):
		if solutionVector[i]:
			d[i] = graphDictionary[i]
	V = length ** 2
	n = getNodes(d)
	G = solutionVector.count(1)
	return n/V + 1/(V*G)