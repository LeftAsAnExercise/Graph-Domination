def latticemaker(n):
	latticelist=[]
	for x in range(n):
		for y in range(n):
			latticelist.append([x,y])

	return latticelist
def moveset(r,s):
	return [[r,s],[r,-s],[-r,-s],[-r,s],[s,r],[s,-r],[-s,-r],[-s,r]]
def vectoradd(n,k):
	placeholder=n
	for i in range(len(placeholder)):
	  placeholder[i]+=k[i] 
	   
	return placeholder

def horsegraph(n):
	#this isn't done
	lattice=latticemaker(n)
	print(lattice)
	print("__________")
	movesets=moveset(1,2)
	for m in lattice:
		print(m)
		print("above is m")
		for k in movesets:
			Ll=vectoradd(m,k)
			if (Ll[0]>=0 and Ll[0]<=n-1) and (Ll[1]>=0 and Ll[1]<=n-1):
				print(Ll)
				
				continue
			else:
				continue
	return 


	
def rsLeaperGraph(n,r,s):
	lattice=latticemaker(n)
	banana=moveset(r,s)
	print(lattice)
	for x in range(n):
		for y in range(n):
			
			for k in banana:
				if vectoradd([x,y],k) in lattice:
					print("_______")
					print(vectoradd([x,y],k))
					print("yes")
					continue
				else:
					continue
	return

			
rsLeaperGraph(40,1,2)
