def tup_string(tup):
    return ''.join(tup)

# Testing
print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))  # Should print "exercises"

"""
Solution Explanation:

The function tup_string takes in a tuple as input. It uses the built-in join() function on the tuple to convert it into a string. The join() function is a string method that concatenates the elements of an iterable (like a tuple) into a string.

The join() function is called on the string ''.join(tup). The '' is the delimiter that is used to join the elements of the tuple. Since we're using '', the elements of the tuple are concatenated without any space in between.

The function then returns the resulting string.
"""
<jupyter_output>
exercises
<jupyter_text>
Q2
<jupyter_code>
