def min_val(lst):
    return min(lst, key=lambda x: (isinstance(x, int), x))

print(min_val(['Python', 3, 2, 4, 5, 'version']))

# Output: 2

# Explanation:
# The function min_val takes a list as input. 
# The min function is called on the list with a key argument lambda function. 
# The lambda function returns a tuple. The first element of the tuple is a boolean indicating whether the item is an integer or not. 
# The second element of the tuple is the item itself. 
# This way, the min function first sorts the items based on whether they are integers or not (True comes first because it's a boolean), 
# and then sorts the items of the same type based on their values. 
# So, for example, in the list ['Python', 3, 2, 4, 5, 'version'], 2 is the smallest integer, so it's returned by the function.
<jupyter_output>
2
<jupyter_text>
