def remove_nested(t):
    return tuple(i for i in t if not isinstance(i, tuple))

print(remove_nested((1, 5, 7, (4, 6), 10)))

# Output:
# (1, 5, 7, 10)

# This solution uses Python's built-in isinstance function to check if each element of the tuple is a tuple. If it is, it is ignored in the new tuple; if it's not, it's included.
<jupyter_output>
(1, 5, 7, 10)
<jupyter_text>
Question 2
<jupyter_code>
