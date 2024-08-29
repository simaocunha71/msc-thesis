def find_substring(lst, s):
    return any(s in i for i in lst)

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))

#Output: True

"""
In this function, we use the built-in function any(), which returns True if at least one element of an iterable is true. 
We pass a generator expression to this function that checks if string s is a substring of any string in the list.
"""
<jupyter_output>
True
<jupyter_text>
Q2:
<jupyter_code>
