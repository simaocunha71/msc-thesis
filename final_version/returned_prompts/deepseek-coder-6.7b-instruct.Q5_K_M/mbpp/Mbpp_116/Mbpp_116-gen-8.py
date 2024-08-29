def tuple_to_int(t):
    return int(''.join(map(str, t)))

print(tuple_to_int((1,2,3))) # returns 123

Explanation:
The function `tuple_to_int` takes a tuple `t` as input. 
`map(str, t)` converts each element in the tuple into a string.
`''.join()` joins these string elements together into one string.
`int()` is then used to convert this string into an integer.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2**
<jupyter_code>
"""
