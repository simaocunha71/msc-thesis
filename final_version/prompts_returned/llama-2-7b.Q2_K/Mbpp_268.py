"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
import math

def find_star_num(n:int):
	# base case
	if n <1 : return None
    # use formula for calculating (2*n-1)!/(2!*(n-1)) to get the number of star numbers
    ndf = int(math.factorial(n)*(2**n)-(2**n-1)*(n-1) )
	# check if n is not divisble by 2, then return None
    if ndf % 2 == 0: 
        # add 1 to the result, so that we will get a star number.
        return find_star_num((n+1))
    else :
        # no need of adding again since n is not divisble by 2 and thus we already have an odd multiple of it as our answer
	return int(find_star_num(n-1)) + ndf//2
