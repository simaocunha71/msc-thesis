```
def extract_values(s):
    return [value.strip('"') for value in s.split('"')]
```


Explanation:
The function `extract_values` takes a string `s` as input and returns a list of values extracted from the string. The values are the strings that are enclosed in quotation marks in the input string.

The function uses the `split` method of the string to split the input string into a list of substrings, using the quotation mark as the delimiter. This results in a list of strings that may or may not be enclosed in quotation marks.

The function then uses a list comprehension to iterate over the list of substrings. For each substring, it uses the `strip` method to remove the quotation marks from the beginning and end of the substring, and adds the resulting string to the output list.

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function works correctly for the given input. It checks that the output of the function is a list containing the strings 'Python', 'PHP', and 'Java', which are the values enclosed in quotation marks in the input string. If the function works correctly, this test will pass. If the function does not work correctly, this test will fail, indicating that there is an error in the function.