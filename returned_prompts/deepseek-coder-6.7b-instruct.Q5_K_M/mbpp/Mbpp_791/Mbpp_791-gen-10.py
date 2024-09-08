def remove_nested(t):
    return tuple(i for i in t if not isinstance(i, tuple))

print(remove_nested((1, 5, 7, (4, 6), 10)))

# 1. The function remove_nested takes a tuple as an argument.
# 2. It uses a generator expression to iterate over the elements of the tuple.
# 3. It checks for each element if it's an instance of tuple using the isinstance function.
# 4. If the element is not a tuple, it's included in the new tuple.
# 5. The function returns the new tuple.
<jupyter_output>
(1, 5, 7, 10)
<jupyter_text>
Q2: Python program to find the sum of all elements in a list using recursion
<jupyter_code>
