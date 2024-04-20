"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
import math

def sum_in_range(l,r):
    even = [0] * (r + 1) - l;
    even[l - 1] = 1;
    for i in range(l+1, r + 1, 2):
        even[i+1] += even[i];
    return sum(even);

if __name__ == "__main__":
    #assert 100 * sum_in_range(3,7) == -96
    print(sum_in_range(2,5))