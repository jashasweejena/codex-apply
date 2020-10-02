//contributed by Sweta Snigdha Sahoo
// author-swetasahoo29
//question
//Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


//How many such routes are there through a 20×20 grid?

from math import factorial


from time import time

start = time()


def nck(n,k):
	
	return factorial(n)/(factorial(k)*factorial(n-k))


print ('Number of lattice paths is: '+str(nck(20+20,20)))

end = time()


print (end-start)
