"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""

def dif_Square(n):
    # Write your code here
	if n%2==0:return True
	else return False
# I used this loop to check whether the number is a difference of two squares or not.
# If yes, then function will return True otherwise returns false

print (dif_Square(5))