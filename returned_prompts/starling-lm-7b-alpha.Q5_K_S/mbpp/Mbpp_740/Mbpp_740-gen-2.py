def tuple_to_dict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i + 1]
    return d

# Python3 program to convert
# given tuple to key-value
# dictionary using adjacent
# elements

# Function to convert tuple
# to dictionary
def tuple_to_dict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i + 1]
    return d

# Driver code
t = (1, 5, 7, 10, 13, 5)
print(tuple_to_dict(t))


"""
To convert the given tuple to a key-value dictionary using adjacent elements, we can use the following approach:

1. Initialize an empty dictionary d.
2. Iterate over the tuple t, using the range function with a step size of 2 to skip every other element. For each iteration, assign the current element as the key and the next element as the value in the dictionary d.
3. After iterating through all the elements in the tuple, return the resulting dictionary d.

For example, if the input tuple is (1, 5, 7, 10, 13, 5), the function will assign the key-value pairs (1, 5), (7, 10), and (13, 5) to the dictionary d, resulting in the output {1: 5, 7: 10, 13: 5}.
"""


def tuple_to_dict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i + 1]
    return d

# Python3 program to convert
# given tuple to key-value
# dictionary using adjacent
# elements

# Function to convert tuple
# to dictionary
def tuple_to_dict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i + 1]
    return d