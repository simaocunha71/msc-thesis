You can use the built-in sorted function in Python, which sorts the elements in a list based on the input function. In this case, you can convert each string to an integer and then sort based on that. Here is the solution:

```Python
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
```

This function works by first converting each string in the list to an integer using the map function. The map function applies a function to every item in an input and returns a list of the results. In this case, the function is int, which converts a string to an integer. Then, the sorted function is used to sort the list of integers. The sorted function returns a new list containing all items from the input list in ascending order. 

The unit test provided ensures that the function works correctly:

```Python
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
```



This function will work correctly for any list of strings that can be converted to integers, and will sort them in ascending order. If the list contains non-numeric strings, the function will raise a ValueError when it tries to convert them to integers. You might want to add error handling to deal with this situation, depending on your specific requirements. 

Here is an example of how you could add error handling:

```Python
def sort_numeric_strings(lst):
    try:
        return sorted(map(int, lst))
    except ValueError:
        return "Error: The list contains non-numeric strings"
```


This version of the function will return an error message if the list contains non-numeric strings, rather than raising an exception. You could also choose to raise a custom exception, or to skip over the non-numeric strings and continue with the rest of the list. The choice will depend on your specific requirements. 