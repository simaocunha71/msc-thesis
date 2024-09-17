```
def check_Consecutive(lst):
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```
The function `check_Consecutive` checks if the given list contains consecutive numbers. It does this by comparing each element in the list with the next one. If all elements in the list are consecutive, the function returns `True`; otherwise, it returns `False`. The function uses the `all` function and a generator expression to check if all elements in the list are consecutive. The `range(len(lst)-1)` ensures that we don't go out of bounds when checking the last element in the list. The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function correctly identifies a list of consecutive numbers. 














```
def check_Consecutive(lst):
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```


```
assert check_Consecutive([1,2,3,4,5]) == True
```


```
assert check_Consecutive([1,2,3,4,6]) == False
```


```
assert check_Consecutive([1,3,5,7,9]) == False
```


```
assert check_Consecutive([1,2,4,5,6]) == False
```


```
assert check_Consecutive([]) == True
```


```
assert check_Consecutive([1]) == True
```


```
assert check_Consecutive([1,1,1,1]) == True
```


```
assert check_Consecutive([1,2,3,5,6]) == False
```


```
assert check_Consecutive([1,2,3,4,5,6]) == True
```


```
assert check_Consecutive([1,3,5,7,9]) == False
```


```
assert check_Consecutive([1,2,3,4,6,7,8]) == True
```


```
assert check_Consecutive([1,2,3,4,5,6,7,8,9]) == True
```


```
assert check_Consecutive([1,2,4,5,6,7,8,9]) == False
```


```
assert check_Consecutive([1,2,3,4,5,6