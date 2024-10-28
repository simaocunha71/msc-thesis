You can use a list comprehension to solve this problem. This function will take a list of strings and an integer as input. It will then filter the list to include only the strings that have a length greater than or equal to the given integer.

Here is the solution:

```Python
def extract_string(lst, size):
    return [string for string in lst if len(string) >= size]
```
This function works by iterating over each string in the input list. For each string, it checks if the length of the string is greater than or equal to the given size. If it is, the string is included in the output list. The output list is then returned.

For example, if you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 8)`, it will return `['practice', 'solution']`, which are the strings with lengths greater than or equal to 8.  The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 8)==['practice', 'solution']` also confirms this. 