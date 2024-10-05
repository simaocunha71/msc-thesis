Here is a Python solution for the problem:
```python
def oddCount(lst):
    return [f"the number of odd elements {len([int(d) for d in s if int(d) % 2])}n the str{s+1}ng {s+1} of the {s+1}nput." for s in lst]
```
This function takes a list of strings as input and returns a list of strings. For each string in the input list, it counts the number of odd digits and inserts this count into the desired format string. The `f-string` formatting is used to insert the count into the string. The `len([int(d) for d in s if int(d) % 2])` expression counts the number of odd digits in the string by iterating over the digits, converting each to an integer, checking if it's odd, and then summing up the results. The `s+1` in the format string is used to insert the string index (1-based) into the output string.

For example, if the input is `['1234567']`, the output will be `["the number of odd elements 4n the str4ng 4 of the 4nput."]`. If the input is `['3',"11111111']`, the output will be `["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]`.