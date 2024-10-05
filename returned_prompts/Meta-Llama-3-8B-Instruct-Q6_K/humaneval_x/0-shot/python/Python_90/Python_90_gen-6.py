```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    min_val = min(lst)
    if lst.count(min_val) > 1:
        return None
    return min(x for x in lst if x > min_val)
```


Explanation:
This function first checks if the list has less than 2 elements. If it does, it returns None because there is no 2nd smallest element. It then finds the minimum value in the list. If the minimum value appears more than once in the list, it means that the list has duplicate values, so it returns None. Finally, it uses a generator expression to find the smallest value greater than the minimum value. This value is the 2nd smallest element in the list. If the list is empty or has only one element, it returns None. 

Example usage:
```
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None
```



Please note that the function may not work correctly if the list contains non-integer values or if the list is very large. In such cases, you might want to sort the list and then return the second smallest value. However, the function as written will work correctly for the specific requirements of the problem. 

Also, the function has a time complexity of O(n) because it needs to iterate over the list to find the minimum value and then iterate again to find the next smallest value. If you need a more efficient solution, you could sort the list and then return the second smallest value, which would have a time complexity of O(n log n). However, the problem statement does not require the function to be efficient, so the current solution is sufficient. 