The task is to sort a list of strings containing numbers numerically. 

The given unit test suggests that the list can contain negative numbers as well. 

Here's a Python solution using the built-in sorted function and the int function to convert the strings to integers:

```Python
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
```

This function works by first converting each string in the list to an integer using the map function. Then, it sorts the list of integers using the sorted function. The result is a sorted list of integers. 

For example, if we call `sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500'])`, the function will return `[-500, -12, 0, 4, 7, 12, 45, 100, 200]`, which is the sorted list of integers. 

This function assumes that the input list only contains strings that can be converted to integers. If the list can contain strings that cannot be converted to integers (like 'abc'), you might want to add some error checking code to handle this situation. 