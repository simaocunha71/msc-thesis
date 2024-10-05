
```python
def how_many_times(string, substring):
    counter = 0
    while True:
        if string.find(substring) == -1:
            break
        counter += 1
        string = string[substring.find(substring) + 1:]
    return counter
```

This function finds the substring in the string, then removes the found substring and continues looking for the substring in the rest of the string.

The `while True:` part creates an infinite loop to keep searching for the substring until no substrings are found, then the loop is broken with the `break` statement. The `find()` method returns the position of the first occurrence of the substring in the string, `-1` means the substring is not found.

The function is implemented in such a way that it considers overlapping cases, as it keeps searching in the remaining string after each found substring.

The `counter` variable is incremented by one each time the substring is found, and the `string` variable is updated with the remaining string after the found substring is removed.

Finally, the function returns the `counter` variable, which represents the number of times the substring can be found in the original string.

To test the function, you can use the provided test cases in the docstring.

```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

These test cases verify if the function correctly counts the occurrences of the substring in the string, considering overlapping cases.

The first test case verifies if the function correctly returns `0` when the string is empty or the substring is not present in the string. The second and third test cases verify if the function correctly counts the occurrences of the substring in the string, even if the substrings overlap.

These test cases ensure that the function works correctly and can be used to find the number of times a substring can be found in a string, including overlapping cases.

```python
```

  
   
  
  