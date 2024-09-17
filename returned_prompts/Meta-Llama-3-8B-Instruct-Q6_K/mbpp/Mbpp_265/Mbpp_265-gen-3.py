```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```


The provided unit test `assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]` suggests that the function should split the list into sublists of length `n` and return a list of these sublists. 

Here's how you can achieve this using list comprehension. The expression `range(0, len(lst), n)` generates indices from 0 to the length of the list, stepping by `n`. For each index `i`, `lst[i:i+n]` generates a sublist of `lst` starting from `i` and ending at `i+n`. The result is a list of these sublists. 

This function assumes that `n` is less than or equal to the length of the list. If `n` is greater than the length of the list, the function will return a list containing the original list. If `n` is zero, the function will return an empty list. If `n` is negative, the function will return an empty list. 

This function is case-sensitive and will treat uppercase and lowercase letters as different characters. If you want to split the list based on the characters, you can convert the list to lowercase or uppercase before splitting it. 

This function does not handle non-string elements in the list. If the list contains non-string elements, they will be included in the sublists as is. If you want to handle non-string elements, you can modify the function to filter them out or convert them to a specific format. 

This function does not handle empty lists. If the input list is empty, the function will return an empty list. If you want to handle empty lists differently, you can modify the function to return a specific value or raise an exception. 

This function does not handle lists of lists. If the input list contains sublists, the function will treat them as single elements. If you want to handle lists of lists, you can modify the function to recursively split the sublists. 

This function does not handle non-