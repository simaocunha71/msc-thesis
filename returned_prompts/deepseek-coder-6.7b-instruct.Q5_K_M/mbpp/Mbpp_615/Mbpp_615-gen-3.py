
def average_tuple(tuples):
    averages = []
    for tup in tuples:
        averages.append(sum(tup) / len(tup))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

"""
Explanation:

The function `average_tuple` takes a tuple of tuples as input. It iterates over each tuple in the input, calculates the average (by summing the elements and dividing by the number of elements) and appends this average to a list `averages`. Finally, it returns the list of averages.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 3: Write a Python function to sort a list of tuples by the last element of each tuple.
<jupyter_code>
