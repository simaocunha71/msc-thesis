def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        for num in t:
            total += num
    return total

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))

# 30

"""
The function 'cummulative_sum' takes a list of tuples as input. It then iterates over each tuple, adding each number in the tuple to a running total. It returns the total at the end.
"""


# 2. Write a function named 'filter_positive_even' that takes a list of numbers as input and returns a list of only the positive even numbers from the input list.

