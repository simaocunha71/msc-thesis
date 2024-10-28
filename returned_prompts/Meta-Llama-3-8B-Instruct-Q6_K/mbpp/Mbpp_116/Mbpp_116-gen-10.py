The problem asks to write a function that takes a tuple of positive integers and returns a single integer. 

However, the problem does not specify the base of the output integer. 

Thanks to the unit test `assert tuple_to_int((1,2,3))==123`, we can assume that the output integer should be in base 10. 

Here is the Python solution:
```
def tuple_to_int(t):
    return int(''.join(map(str, t)))
``` 
This function first converts each integer in the tuple to a string using the `map` function. Then it joins these strings together into a single string using the `join` function. Finally, it converts this string into an integer using the `int` function. 

For example, if the input tuple is `(1,2,3)`, the function will convert it to the string `'123'` and then to the integer `123`.  This solution passes the given unit test.  However, it may not work correctly if the input tuple contains integers larger than the maximum value that can be represented by a string in Python.  In such cases, you might need to use a different approach.  For example, you could convert the integers to a string in base 26 (since there are 26 letters in the alphabet) and then convert the resulting string to an integer.  However, this approach would require more complex code and might not be necessary for the given unit test.  Therefore, the given solution is a simple and effective way to solve the problem. 