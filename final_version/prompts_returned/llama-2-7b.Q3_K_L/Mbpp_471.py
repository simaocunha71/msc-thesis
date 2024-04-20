"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
from math import *
def find_remainder(a,n):
    def prod(x):
        return x%n
    ans=prod(*[int(i) for i in a])
    return int(ans)


if __name__ == "__main__":
   print(find_remainder([100, 10, 5, 25, 35, 14], 11))