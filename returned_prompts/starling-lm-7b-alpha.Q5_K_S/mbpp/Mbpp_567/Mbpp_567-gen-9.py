
Here is a Python function that checks whether a specified list is sorted or not:

```python
def issort_list(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True
```

To use this function, you can call it with a list as an argument, like this:

```python
print(issort_list([1,2,4,6,8,10,12,14,16,17]))  # Returns: True
print(issort_list([1,2,4,6,8,10,12,14,17,16]))  # Returns: False
```

The function checks each element in the list with its next element. If it finds an element that is greater than its next element, it returns False, indicating that the list is not sorted. If the function goes through the entire list without finding any such pair of elements, it returns True, indicating that the list is sorted.

In the provided example, the first call to the function returns True because all elements in the list are in increasing order. The second call to the function returns False because the element