```
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
```


This function uses Python's built-in `sorted` function to sort the list of strings. The `map` function is used to convert each string in the list to an integer, allowing the `sorted` function to sort them numerically. The result is a new list that contains the elements of the original list in numerical order. 

The unit test `assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]` shows that the function correctly sorts the list of strings numerically. 