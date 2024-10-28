```
def remove_whitespaces(s):
    return s.replace(' ', '')
``` 

This function uses the built-in string method `replace()` to replace all occurrences of a whitespace character with an empty string, effectively removing them. 

The unit test provided ensures that the function works correctly by comparing the output of the function with the expected result. The test checks if the function removes all whitespaces from the input string and returns the expected output. 

The function is then used to remove whitespaces from the given string and returns the result. 

For example, if the input string is ' Google    Flutter ', the function will return 'GoogleFlutter'. 

This solution assumes that the input string contains only ASCII characters and does not consider any other type of whitespace characters. If the function needs to handle other types of whitespace characters, it can be modified accordingly. 

The time complexity of this function is O(n), where n is the length of the input string, because it needs to iterate over the entire string to replace all occurrences of whitespace characters. The space complexity is O(1), because it only uses a constant amount of space to store the output string. 