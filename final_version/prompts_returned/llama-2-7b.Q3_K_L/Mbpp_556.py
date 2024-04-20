"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_odd_pair(arr, target):
    sum = sum((i ^ j for i,j in itertools.combinations(arr, 2)) & target)
    print(sum)
    return sum
