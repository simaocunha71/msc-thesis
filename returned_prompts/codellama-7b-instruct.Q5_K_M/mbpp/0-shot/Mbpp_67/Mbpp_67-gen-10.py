"""
We are given Bell numbers as follows:

B(0) = 1
B(1) = 1
B(n) = B(n-1) + B(n-2) for n > 1

We can use the above recurrence to partition a set of Bell numbers.
We need to find all the combinations of sets of Bell numbers that add up to the total Bell number.
"""

bell_number = lambda n: 1 if n<3 else bell_number(n-1)+bell_number(n-2)

def partition(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return sum([partition(n-i)*partition(i) for i in range(n)])

assert partition(2)==2