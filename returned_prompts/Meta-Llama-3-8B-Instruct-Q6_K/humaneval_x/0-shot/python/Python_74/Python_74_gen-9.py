```
def total_match(lst1, lst2):
    total_chars1 = sum(len(s) for s in lst1)
    total_chars2 = sum(len(s) for s in lst2)
    if total_chars1 < total_chars2:
        return lst1
    elif total_chars1 > total_chars2:
        return lst2
    else:
        return lst1
```


This function works by calculating the total number of characters in each list using a generator expression and the built-in `sum` function. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list. This function works for lists of any length and can handle lists with duplicate strings. It is case sensitive, so 'hi' and 'Hi' are considered different strings. 

For example, if you call `total_match(['hi', 'admin'], ['hI', 'Hi'])`, the function will return `['hI', 'Hi']` because 'hI' and 'Hi' are considered different strings. If you want the function to be case insensitive, you can convert each string to lower case or upper case before comparing them. 

The function also works correctly when one or both lists are empty, as shown in the example `total_match([], [])`. It returns an empty list in this case. 

The function is also able to handle lists with non-string elements, such as integers or floats. However, it will raise an error if a list contains non-string elements, because the `len` function is not defined for non-string elements. You can add error handling to the function if you want it to handle non-string elements. 