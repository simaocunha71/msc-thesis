"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
import bisect

def min(lst):
    return min(lst,[key for key,value in lst])

input = [str(s) for s in input()]
n = int(input())
lst = [int(i) for i in input()]

ans = min_val = min([max(x-1000, 0) for x in lst])
for n in ans:
    print(n,' is the minimum value')