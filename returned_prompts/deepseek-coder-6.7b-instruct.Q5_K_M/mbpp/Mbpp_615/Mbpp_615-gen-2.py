
def average_tuple(tuples):
    averages = []
    for tup in tuples:
        averages.append(sum(tup)/len(tup))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# or you can use list comprehension to make it more pythonic:

def average_tuple(tuples):
    return [sum(tup)/len(tup) for tup in tuples]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

"""
The function works by iterating over each tuple in the input and summing its elements, then dividing by the number of elements to compute the average. It appends these averages to a list which is returned as the result.
"""
<jupyter_output>
[30.5, 34.25, 27.0, 23.25]
[30.5, 34.25, 27.0, 23.25]
<jupyter_text>
Problem 3
<jupyter_code>
