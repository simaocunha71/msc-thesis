def sum_of_digits(numbers):
    s = 0
    for i in numbers:
        while i > 0:
            s += i % 10
            i = i // 10
    return s

# assert sum_of_digits([10,2,56])==14
# print(sum_of_digits([10,2,56]))
# print(sum_of_digits([100,2,56]))
# print(sum_of_digits([1000,2,56]))

"""
The above code can be optimized using built-in Python function map() and sum(), and list comprehension.
"""

def sum_of_digits(numbers):
    return sum(map(lambda x: sum(int(i) for i in str(x)), numbers))

print(sum_of_digits([10,2,56]))
print(sum_of_digits([100,2,56]))
print(sum_of_digits([1000,2,56]))


"""
The above code can be optimized again using Python built-in function reduce().
"""

from functools import reduce

def sum_of_digits(numbers):
    return reduce(lambda x, y: x + sum(int(i) for i in str(y)), numbers)

print(sum_of_digits([10,2,56]))
print(sum_of_digits([100,2,56]))
print(sum_of_digits([1000,2,56]))


"""
The above code can be optimized using Python built-in function itertools.chain() and itertools.imap()
"""

from itertools import chain, imap

def sum_of_digits(numbers):
    return sum(imap(lambda x: sum(int(i) for i in str(x)), list(chain(*numbers))))

print(sum_of_digits([10,2,56]))
print(sum_of_digits([100,2,5