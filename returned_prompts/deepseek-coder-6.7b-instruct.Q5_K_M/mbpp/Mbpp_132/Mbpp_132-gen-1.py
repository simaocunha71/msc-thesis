
def tup_string(tup):
    return ''.join(tup)

print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))

"""
Output:
"exercises"
"""

This function works by using the join() method on the tuple. The join() method takes all items in an iterable and joins them into one string. The string it uses to join the items is specified as a string literal inside the parentheses. In this case, it's an empty string '', so the items are joined without any character in between.
<jupyter_output>
<empty_output>
<jupyter_text>
