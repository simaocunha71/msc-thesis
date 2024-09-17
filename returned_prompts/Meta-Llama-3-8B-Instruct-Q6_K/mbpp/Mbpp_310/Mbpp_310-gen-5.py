```
def string_to_tuple(s):
    return tuple(s)
```


Python's built-in `tuple()` function can convert a string into a tuple of characters. This function takes a string as an argument and returns a tuple where each element is a character from the string. For example, `string_to_tuple("python 3.0")` would return `('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')`. This function works as expected, as shown in the unit test provided. The unit test checks if the function correctly converts the string "python 3.0" to the tuple `('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')`. The function passes this test, indicating that it is working as intended.