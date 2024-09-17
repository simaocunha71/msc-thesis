```
def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result
```


The problem asks to write a function that removes consecutive duplicates from a given list. 

The provided unit test `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]` helps to understand the problem better. 

The function should return a list where consecutive duplicates are removed. 

Here's the solution:
```
def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result
```
This function iterates over the input list. If the result list is empty or the current element is different from the last element in the result list, it appends the current element to the result list. This way, consecutive duplicates are removed. 





Here is how you can use this function:
```
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))
```
This will output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```





This function works by iterating over the input list and appending each element to the result list only if it is different from the last element in the result list. This way, consecutive duplicates are removed from the result list. The function returns the result list after iterating over the input list.