The problem is asking to create a function that takes a tuple of positive integers as input and returns a single integer. The single integer should be the concatenation of the strings representing the input tuple.

For example, if the input tuple is (1, 2, 3), the output should be 123.

Here's a Python function that solves this problem:

```python
def tuple_to_int(t):
    return int(''.join(map(str, t)))
```

This function works by first using the map function to convert each integer in the tuple to a string. It then joins these strings together into a single string using the join function. Finally, it converts this string to an integer using the int function.

The unit test `assert tuple_to_int((1,2,3))==123` ensures that the function works correctly. This test checks that when the input tuple is (1, 2, 3), the output is indeed 123. If the function is implemented correctly, this test should pass. If the function is implemented incorrectly, this test will fail, indicating that there is a bug in the function. 