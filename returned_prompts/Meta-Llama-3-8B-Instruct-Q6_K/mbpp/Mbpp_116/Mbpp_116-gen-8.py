The problem is asking to write a function that takes a tuple of positive integers as input and returns a single integer. The single integer is formed by concatenating the strings representation of the integers in the tuple.

The unit test `assert tuple_to_int((1,2,3))==123` suggests that the function should work in this way.

Here is the solution in Python:
```python
def tuple_to_int(t):
    return int(''.join(map(str, t)))
```
This function uses the `map` function to convert each integer in the tuple to a string, and then joins these strings together into a single string. The `int` function is then used to convert this string back into an integer. 

For example, if the input tuple is `(1,2,3)`, the function will first convert each integer to a string: `['1', '2', '3']`. Then it will join these strings together: `'123'`. Finally, it will convert this string back into an integer: `123`. 

So the output of `tuple_to_int((1,2,3))` will be `123`. 