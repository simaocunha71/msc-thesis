def tuple_str_int(s):
    return eval(s)

print(tuple_str_int("(7, 8, 9)"))

# Alternatively, you could use ast.literal_eval
import ast

def tuple_str_int(s):
    return ast.literal_eval(s)

print(tuple_str_int("(7, 8, 9)"))

# Both of these will return the tuple (7, 8, 9)

# These solutions are safe because they use eval or ast.literal_eval to safely convert a string to a Python literal.
# However, be careful because the eval and ast.literal_eval functions can evaluate any arbitrary Python code,
# so they should not be used with untrusted input.

# If you're sure that the input is always a string representation of a tuple of integers,
# then either of these solutions is safe to use.
<jupyter_output>
(7, 8, 9)
(7, 8, 9)
<jupyter_text>
Problem 6
<jupyter_code>
