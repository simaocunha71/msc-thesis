```
def frequency(lst, num):
    return lst.count(num)
```
This function uses the built-in count method of Python lists, which returns the number of occurrences of its argument in the list. If the number is not found in the list, it returns 0. The unit test `assert frequency([1,2,3], 4) == 0` ensures that the function returns 0 when the number is not found in the list. 