"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
import math

def bell_number(n):
    if not n: return 1
    return bell_number(n-1)*bell_number(n-1)+bell_number(n-2)

def bell_partition(n, k):
    """Return a list of all the k partitions for set n.
    The first element is the number of ways to choose an order in the k partitions."""
    return list(map(lambda l: sum([bell_number(n-l)for i in range(len(l))]), combinations_with_replacement(range(1,k+1), k)))

def test():
    print("Testing bell_partition")
    assert bell_partition(2, 2) == (19680,)
    assert bell_partition(3, 2) == (48,)
    assert bell_partition(3, 3) == (135, 179, 247)
    
if __name__=='__main__':
    test()