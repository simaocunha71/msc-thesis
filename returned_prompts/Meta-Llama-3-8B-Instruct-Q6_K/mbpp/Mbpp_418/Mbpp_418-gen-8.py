```
def Find_Max(lst):
    return max(lst, key=len)
```
The function `Find_Max` takes a list of lists as an argument and returns the list with the maximum length. The `max` function is used with a `key` argument set to `len`, which means that the list with the maximum length is selected. The unit test provided in the question `assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']` ensures that the function is working correctly.  If the input list is empty, the function will raise an exception. To avoid this, we can add a condition to check if the list is empty before calling the `max` function. 

Here is the updated function:
```
def Find_Max(lst):
    if not lst:
        return None
    return max(lst, key=len)
```  This function will return `None` if the input list is empty. You can modify it to return a default value or to raise an exception if you prefer. 