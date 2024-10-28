```
def min_val(lst):
    return min(i for i in lst if type(i) in [int, float])
```
The function `min_val` takes a list `lst` as input and returns the minimum value from the list. It uses a generator expression to iterate over the list, selecting only the elements that are integers or floats using the `type(i) in [int, float]` condition. The `min` function is then used to find the minimum value from the selected elements. 

The unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2` ensures that the function works correctly by checking if the minimum value of the list `['Python', 3, 2, 4, 5, 'version']` is `2`, which is the correct result. 

Note: This function will not work correctly if the list contains negative numbers or decimal values. It will only work correctly if the list contains only positive integers. If you want to handle negative numbers and decimal values, you would need to modify the function accordingly. 