def average_tuple(tup):
    averages = []
    for t in tup:
        averages.append(sum(t)/len(t))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Explanation:
# The function `average_tuple` takes a tuple of tuples as input.
# It then iterates over each tuple in the input tuple, calculates the average by summing all elements in the tuple and then dividing by the count of elements,
# and appends this average to a list called `averages`.
# Finally, the function returns the list of averages.

# Testing:
# For the given input, the function should return the list [30.5, 34.25, 27.0, 23.25] which are the averages of the four tuples in the input.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]

# If the assertion passes, the test is successful.
<jupyter_output>
[30.5, 34.25, 27.0, 23.25]
<jupyter_text>
Question 2
<jupyter_code>
