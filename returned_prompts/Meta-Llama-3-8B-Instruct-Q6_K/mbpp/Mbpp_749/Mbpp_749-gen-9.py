```
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
``` 

This function uses the built-in Python function sorted() to sort the list of strings. The map() function is used to convert each string in the list to an integer, which is then sorted numerically. 

The unit test provided ensures that the function works correctly. The test case checks if the output matches the expected sorted list of integers. 

The function will work correctly for a list of strings containing only positive or negative integers. If the list contains non-numeric strings, the function will raise a ValueError. 

For example, if the input list is ['4','12','45','7','0','100','200','-12','-500'], the output will be [-500, -12, 0, 4, 7, 12, 45, 100, 200]. 

Note: The built-in sorted() function in Python is stable, meaning that when multiple records have the same key, their original order is preserved. This ensures that the function works correctly for lists containing duplicate strings. 