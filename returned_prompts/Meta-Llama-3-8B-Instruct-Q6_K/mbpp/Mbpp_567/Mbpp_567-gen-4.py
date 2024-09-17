```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```    
    This function checks if a list is sorted or not. It does this by comparing each element in the list to the next one. If all elements are in order, it returns True, meaning the list is sorted. If any two elements are not in order, it returns False, meaning the list is not sorted.
    The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` ensures that the function returns True for a list that is indeed sorted.
```python
print(issort_list([1,2,4,6,8,10,12,14,16,17]))  # returns: True
print(issort_list([1,2,4,6,8,10,12,14,17,16]))  # returns: False
```    
    Output:
```
True
False
```    
    This shows that the function correctly identifies a sorted list and a list that is not sorted.    
```python
```    
    Note: This function does not check for any other types of sorting, such as reverse sorting. If you want to check for reverse sorting, you can modify the function accordingly. For example, you could change the comparison to `lst[i] >= lst[i+1]` to check for reverse sorting.    
```python
```    
    Also, this function assumes that the list is not empty. If you want to check for empty lists as well, you can add a simple check at the beginning of the function. For example:
```python
def issort_list(lst):
    if not lst:
        return True  # or False, depending on your desired behavior for empty lists
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```    
    This way, the function will return True for empty lists, assuming that an empty list is considered sorted. If you want to return False for empty lists, you can simply remove this check.    
```python
```    
    Finally, it's worth noting that this function has a time complexity of O(n), where n is the length of the list. This is because it needs to iterate over the entire list to check if it's sorted. If you're working with very large lists, you may want to consider