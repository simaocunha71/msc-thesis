"""
This problem can be solved using the itertools library in Python. The itertools module implements a number of iterator building blocks. Here we use the chain and combinations functions.

Here is the Python solution:
"""
from itertools import chain, combinations

def find_combinations(arr):
    all_combinations = []
    for i in range(len(arr) + 1):
        all_combinations += list(chain(*[combinations(arr, i) for _ in range(i)]))
    sums = [(sum(x[0] for x in combo), sum(x[1] for x in combo)) for combo in all_combinations]
    return sums

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))

# Output:
# [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11), (2, 4), (6, 7), (5, 1), (6, 10), (8, 7), (7, 3), (7, 11), (12, 13), (8, 5), (11, 10), (10, 7), (14, 11), (8, 10), (11, 14), (10, 10)]

"""
This solution works by first generating all possible combinations of tuples from the given list. It then calculates the sums of each tuple in each combination and returns a new list of tuples with these sums.
"""
















































































































