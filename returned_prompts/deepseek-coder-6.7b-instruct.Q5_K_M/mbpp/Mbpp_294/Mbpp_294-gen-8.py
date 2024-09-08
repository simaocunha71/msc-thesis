def max_val(lst):
    return max(lst, key=lambda x: (isinstance(x, int), x))

print(max_val([3, 2, 4, 5]))

# The function above uses the built-in Python function max() with a custom key. This key is a function that returns a tuple. The tuple consists of two parts: a boolean indicating if the current item is an integer, and the item itself. 

# The boolean is used to sort the items first by type (integers first) and then by value. This means that the max() function will first try to find the maximum integer in the list, and if there are no integers in the list, it will return the maximum non-integer item.
<jupyter_output>
5
<jupyter_text>
