You can solve this problem by using Python's built-in string methods. The `re` module can be used to find all occurrences of a pattern in a string and return them as a list.

Here is the solution:

```Python
import re

def extract_values(s):
    return re.findall(r'"([^"]*)"', s)
```

This function uses the `re.findall` method to find all occurrences of the pattern `'"([^"]*)"'` in the string `s`. The pattern `'"([^"]*)"'` matches any character that is not a double quote `"` (captured in a group), enclosed in double quotes. The `re.findall` method returns a list of all non-overlapping matches of this pattern in the string, as a list of strings.

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function works correctly. It checks that the function returns the expected list of values when given the string `"Python", "PHP", "Java"`. If the function is working correctly, this test will pass. If the function is not working correctly, this test will fail and provide an error message that will help you to identify the problem.

You can run this function with the unit test to ensure it works correctly:

```Python
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
print(extract_values('"Python", "PHP", "Java"'))
```


This will print `['Python', 'PHP', 'Java']` and will not raise an AssertionError, which means that the function is working correctly.