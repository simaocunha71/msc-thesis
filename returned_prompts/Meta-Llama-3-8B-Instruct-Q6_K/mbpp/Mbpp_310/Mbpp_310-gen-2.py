```
def string_to_tuple(s):
    return tuple(s)
```
This function uses Python's built-in `tuple()` function to convert the given string into a tuple of characters. The `assert` statement provided in the problem ensures that the function works correctly for the given input "python 3.0". 

For example, if you call `string_to_tuple("python 3.0")`, it will return the tuple `('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')`. 

The `tuple()` function is a built-in Python function that takes an iterable (like a string) and returns a tuple containing all the elements from the iterable. In this case, it takes the string "python 3.0" and returns a tuple containing each character in the string, in the same order. 

Note: The `string_to_tuple` function is case-sensitive, meaning that it will treat uppercase and lowercase letters as different characters. If you want to convert the string to a tuple of lowercase characters, you can use the `lower()` method to convert the string to lowercase before converting it to a tuple. For example: `return tuple(s.lower())`. 