def max_val(lst):
    return max(lst, key=lambda x: (isinstance(x, int), x))

print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Outputs: 5

"""
Explanation:
In the function above, we use the built-in function max(). The key argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In our case, we use a lambda function that returns a tuple. The first element of the tuple is a boolean indicating whether the element is an integer, and the second element is the element itself. The max function then compares these tuples and returns the element with the maximum tuple. In other words, it prioritizes integers over other types.
"""
<jupyter_output>
5
<jupyter_text>
