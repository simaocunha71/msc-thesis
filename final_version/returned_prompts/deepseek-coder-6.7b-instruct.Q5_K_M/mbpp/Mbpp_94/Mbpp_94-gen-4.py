def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

# Output: 'Varsha'

# This function works by using the built-in min function, with the key parameter set to a lambda function that returns the second element of each tuple. The min function then returns the tuple with the smallest second element, and the [0] indexing at the end returns the first element of that tuple.
<jupyter_output>
Varsha
<jupyter_text>
Problem 6:Write a Python function to compute the sum of all the unique elements in a list.
<jupyter_code>
