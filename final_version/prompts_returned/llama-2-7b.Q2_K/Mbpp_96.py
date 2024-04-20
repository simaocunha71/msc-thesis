"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""

def divisor(n):
    # Write your code here
	#return n % 0

	if n >1:
        return n+divisor(n-1) if (n%2==1 and n>1 ) else n%2 == 0 or not (n// 2)
	else:
		return False
