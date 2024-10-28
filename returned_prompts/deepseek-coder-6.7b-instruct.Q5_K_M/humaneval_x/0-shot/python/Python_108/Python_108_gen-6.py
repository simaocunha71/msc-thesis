
def count_nums(arr):
    def sum_digits(n):
        if n < 0:
            return sum(int(d) for d in str(-n)[1:])
        else:
            return sum(int(d) for d in str(n))
    return sum(sum_digits(n) > 0 for n in arr)

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)

This code works by first defining a helper function sum_digits which takes an integer n and returns the sum of its digits. If n is negative, it first converts it to a string, slices off the first character (which is '-'), converts the rest to integers, and then sums them. If n is positive, it converts it to a string, converts each character to an integer, and then sums them.

Then it applies this helper function to each element of arr using a generator expression, converts the resulting boolean values to integers (True becomes 1 and False becomes 0), and sums them up.

This is a very compact way of writing the required logic.
    """
    return sum(sum(int(d) for d in str(n)) > 0 for n in arr)

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
"""
    """
    return sum(sum(int(d) for d in str(n)) > 0 for n in arr)

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
"""

def count_nums(arr):
    def sum_digits(n):
        if n < 0:
            return sum(int(d) for d in str(-n)[1:])
        else:
            return sum(int