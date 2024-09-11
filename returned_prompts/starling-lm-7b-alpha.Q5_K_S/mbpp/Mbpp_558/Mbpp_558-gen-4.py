def digit_distance_nums(n1,n2):
    l1 = list(str(n1))
    l2 = list(str(n2))
    if len(l1)!=len(l2):
        return None
    else:
        return sum(abs(int(l1[i])-int(l2[i])) for i in range(len(l1)))

# Test
assert digit_distance_nums(1,2) == 1

# Another way
def digit_distance_nums_alt(n1,n2):
    return abs(str(n1)[0]-str(n2)[0])+abs(str(n1)[1]-str(n2)[1])

# Test
assert digit_distance_nums_alt(1,2) == 1

# Another way
def digit_distance_nums_alt2(n1,n2):
    return sum(abs(n1%10-n2%10),n1//10,n2//10)

# Test
assert digit_distance_nums_alt2(1,2) == 1







"""
For example, given two numbers 1 and 2, the per-digit difference is 1-2=-1, and the sum of the per-digit difference is -1.

In general, given two numbers n1 and n2, the per-digit difference is the sum of the absolute difference between each digit in the two numbers. For example, the per-digit difference of 123 and 456 is |1-4| + |2-5| + |3-6| = 3.

Write a Python function to find the sum of the per-digit difference between two integers.

Examples:

digit_distance_nums(1, 2) --> 1
digit_distance_nums(123, 456) --> 3

Note:
If the lengths of the two numbers are different, return None.

"""

"""
Correct Solution:
def digit_distance_nums(n1,n2):
    if len(