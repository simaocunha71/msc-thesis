```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```


This function uses list comprehension to create a new list where each string in the input list is reversed. The `s[::-1]` syntax is used to reverse each string. For example, the string "Red" becomes "deR". 

The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` ensures that the function is working correctly. 

The function can be used like this:
```
print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
# Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```


This function assumes that all elements in the input list are strings. If the list can contain non-string values, the function will need to be modified to handle this. For example, it could skip non-string values or raise an error if it encounters a non-string value. 

Here is an example of how you could modify the function to skip non-string values:
```
def reverse_string_list(lst):
    return [s[::-1] if isinstance(s, str) else s for s in lst]
```


This modified function will skip non-string values and leave them unchanged in the output list. For example:
```
print(reverse_string_list(['Red', 'Green', 'Blue', 4, 'White', 'Black']))
# Output: ['deR', 'neerG', 'eulB', 4, 'etihW', 'kcalB']
```


This function will raise a TypeError if it encounters a non-string value that cannot be skipped (for example, a list or a dictionary). If you want to handle this case differently, you will need to add additional error handling code. 





Final Answer: The final answer is `def reverse_string_list(lst): return [s[::-1] for s in lst]`. I hope it is correct.