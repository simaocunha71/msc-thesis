"""
def index_minimum(list_of_tuples):
    return min(list_of_tuples, key=lambda x: x[1])[0]
"""

# Python program to find the minimum value
# of the second element in a list of tuples

# Returns the tuple with the minimum second element
def index_minimum(list_of_tuples):
    min_tuple = min(list_of_tuples, key = lambda x: x[1])
    return min_tuple[0]

# Driver code
list_of_tuples = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
print(index_minimum(list_of_tuples))
# Output: 'Varsha'

# The above code is equivalent to the below code:
# Returns the first element of the tuple with the minimum second element
def index_minimum(list_of_tuples):
    return min(list_of_tuples, key = lambda x: x[1])[0]

# Driver code
list_of_tuples = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
print(index_minimum(list_of_tuples))
# Output: 'Varsha'

# This code is better because it directly returns the first element of the tuple with the smallest second element.
# The other code has to return the tuple and then access the first element of that tuple, which is unnecessary.




