
def cummulative_sum(lst):
    total_sum = 0
    for tup in lst:
        total_sum += sum(tup)
    return total_sum

assert cummulative_sum([(1, 3),  (5, 6, 7),  (2, 6)]) == 30
"""
Explanation:
The function cummulative_sum takes a list of tuples as input.
It initializes a variable total_sum to 0.
Then it iterates over each tuple in the list. For each tuple, it adds the sum of all its elements to total_sum.
Finally, it returns the total_sum.
The assert statement tests if the function works correctly.
"""

