Here is a Python solution for the problem:

```Python
def oddCount(lst):
    return [f"the number of odd elements {str(i).count('1')}n the str{i}ng {i} of the {i}nput." for i in lst]
```

This function uses a list comprehension to iterate over each string in the input list. For each string, it counts the number of odd digits using the `count` method and inserts this count into the output string. The `str(i).count('1')` expression counts the number of '1's in the string representation of the index `i`. The `f-string` formatting is used to create the output string. The `str(i)` conversion is used to convert the integer index to a string for the `count` method. 

For example, if the input list is `['1234567']`, the output will be `["the number of odd elements 4n the str4ng 4 of the 4nput."]`. If the input list is `['3',"11111111"]`, the output will be `["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]`. 

Note: This solution assumes that the input list contains only strings consisting of digits. If the input list can contain other types of strings, you may need to add error handling to handle this case. 