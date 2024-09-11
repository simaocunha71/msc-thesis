```
def concatenate_tuple(t):
    return '-'.join(map(str, t))
```

Explanation:
To solve the problem, we can use the `join()` method to concatenate elements of a tuple by a delimiter. First, we use the `map()` function to convert each element of the tuple to a string. Then, we use the `join()` method to concatenate the elements by the delimiter.
Here's an example of the function in action:
```python
def concatenate_tuple(t):
    return '-'.join(map(str, t))

# Test the function
print(concatenate_tuple(("ID", "is", 4, "UTS")))  # Output: 'ID-is-4-UTS'
```
The `join()` method concatenates the elements of the tuple by the delimiter, resulting in the desired output.

In the provided code, the `map()` function is used to convert each element of the tuple to a string. The `map()` function takes a function and an iterable as arguments. In this case, the function is the `str()` function, which converts a value to a string. The iterable is the tuple `t`. The `map()` function returns an iterator that applies the `str()` function to each element of the tuple.

The `join()` method is then used to concatenate the mapped elements with the delimiter '-'. The `join()` method takes an iterable and a delimiter as arguments. In this case, the iterable is the mapped elements, and the delimiter is '-'. The `join()` method returns a string that is the concatenation of the mapped elements with the delimiter.

Finally, the concatenated string is returned by the `concatenate_tuple()` function.

This solution effectively concatenates each element of the tuple by the delimiter, as required by the problem statement.

For more information, you can refer to the following resources:
- [Joining Strings](http://docs.python.org/2/library/stdtypes.html#str.join)
- [map()](http://docs.python.org/2/library/functions.html#map