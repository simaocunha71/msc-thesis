def tuple_str_int(s):
    return eval(s)

print(tuple_str_int("(7, 8, 9)"))

#OR

def tuple_str_int(s):
    return tuple(map(int, s.strip('()').split(',')))

print(tuple_str_int("(7, 8, 9)"))

#OR

def tuple_str_int(s):
    return tuple(int(i) for i in s[1:-1].split(','))

print(tuple_str_int("(7, 8, 9)"))

#OR

def tuple_str_int(s):
    return tuple(map(int, s[s.find("(")+1:s.find(")")].split(',')))

print(tuple_str_int("(7, 8, 9)"))


#All the above solutions will give you the same output.

"""
tuple_str_int function works by using the eval function to convert the string into a tuple. eval is a built-in Python function that can parse a string and execute it as a Python expression.

In the second solution, we use the split and map functions to split the string into a list of strings, convert each string to an integer with the map function, and then convert the list of integers back into a tuple.

The third solution is similar to the second, but it uses a generator expression instead of a map function to create the tuple.

The last solution is a bit more complex, but it uses the find method to find the start and end of the tuple in the string. It then uses the same split and map functions as the second solution to convert the string into a tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
