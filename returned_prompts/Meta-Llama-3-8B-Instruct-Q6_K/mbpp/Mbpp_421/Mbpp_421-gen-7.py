```
def concatenate_tuple(t):
    return '-'.join(str(i) for i in t)
```
This function takes a tuple `t` as input, iterates over each element in the tuple, converts each element to a string using `str(i)`, and then joins the strings together using the `-` character as the delimiter. The result is a string where each element of the original tuple is concatenated by the delimiter.

The unit test `assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'` ensures that the function works correctly. It checks that the function returns the expected string when given the tuple `("ID", "is", 4, "UTS")` as input. If the function works correctly, this test will pass. If the function does not work correctly, this test will fail, indicating that there is a bug in the function.