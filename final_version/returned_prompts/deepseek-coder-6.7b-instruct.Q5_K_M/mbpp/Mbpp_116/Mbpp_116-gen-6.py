
def tuple_to_int(t):
    str_t = [str(i) for i in t]
    return int(''.join(str_t))

print(tuple_to_int((1,2,3)))

# Expected output: 123

"""
In this function, we first convert each element of the tuple into a string using a list comprehension. 
Then we join these strings together into a single string using the join() method. Finally, we convert the string back into an integer using the int() function and return the result.
"""

"""
This function works because the join() method concatenates all the elements of an iterable (in this case, a list of strings) into a single string, and the int() function converts a string into an integer. 

The tuple_to_int() function takes a tuple of positive integers as input, converts each element to a string using a list comprehension, and then joins them together into a single string. 

Finally, it converts the string back into an integer using the int() function and returns the result.
"""
<jupyter_output>
123
<jupyter_text>
Question 2
<jupyter_code>
