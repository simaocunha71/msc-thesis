```
def occurance_substring(big_string, substring):
    try:
        index = big_string.index(substring)
        return substring, index, index + len(substring)
    except ValueError:
        return None
```
This function uses the `index` method of the string to find the first occurrence of the substring. If the substring is not found, the `index` method raises a `ValueError` exception, which is caught and handled by returning `None`. Otherwise, the function returns a tuple containing the substring, its starting position, and its ending position.

The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function works correctly. It checks that the function returns the substring 'python' at position 0 and ending at position 6 in the string 'python programming, python language'. 

Note: The `index` method returns the index of the first occurrence of the substring. If the substring appears multiple times in the string, this function will only find the first occurrence. If you want to find all occurrences, you would need to use a loop and the `find` method instead. 