"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""

def min_of_three(a,b,c):
    return max(a,max(b,c))