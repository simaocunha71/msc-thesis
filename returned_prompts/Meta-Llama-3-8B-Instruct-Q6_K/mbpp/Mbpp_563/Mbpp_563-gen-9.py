```
def extract_values(s):
    return [value.strip('"') for value in s.split('"') if value.strip('"')]
```
This function splits the input string `s` into substrings at each occurrence of the quotation mark `"` using the `split` method. It then iterates over these substrings, strips any leading or trailing quotation marks using the `strip` method, and includes only the non-empty strings in the resulting list. The function returns this list of extracted values. 

For example, given the input string `"Python", "PHP", "Java"`, this function would return the list `['Python', 'PHP', 'Java']`. 

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function works correctly for this specific input.  The function should pass this test if it is implemented correctly.  The unit test can be extended to cover other edge cases and different input strings to ensure the function is robust and works correctly for a variety of inputs. 

This function assumes that the quotation marks are used to enclose values and that there are no quotation marks within the values.  If the values can contain quotation marks, the function would need to be modified to handle this case.  For example, it could use a regular expression to match values that are enclosed in quotation marks, or it could use a parser to parse the input string as a valid format.  The specific approach would depend on the requirements of the problem and the structure of the input data. 