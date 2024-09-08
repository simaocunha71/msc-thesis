def tuple_to_dict(tup):
    return {tup[i]: tup[i + 1] for i in range(0, len(tup), 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

Explanation:
In this function, we are using dictionary comprehension to create a dictionary. We iterate over the tuple with a step of 2 (i.e., adjacent elements) in a for loop. The key-value pair is then created using the current element and the next element.
"""

"""
