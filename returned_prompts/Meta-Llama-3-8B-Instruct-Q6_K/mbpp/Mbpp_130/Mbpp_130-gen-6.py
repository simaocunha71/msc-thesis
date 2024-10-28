```
def max_occurrences(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return max(freq, key=freq.get)
```



This function works by first creating a dictionary where the keys are the items in the list and the values are the frequencies of those items. It then returns the item with the maximum frequency. 

The unit test provided, `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2`, ensures that the function returns the item with the maximum frequency, which in this case is 2. 

This function assumes that the list is not empty and that all elements are hashable (i.e., they can be used as dictionary keys). If the list is empty or if it contains unhashable elements, the function will raise an exception. 

The time complexity of this function is O(n), where n is the number of items in the list, because it needs to iterate over the entire list to create the frequency dictionary. The space complexity is also O(n), because in the worst case (when all items are unique), the frequency dictionary will contain n items. 





Note: The problem statement is open to interpretation, and there are different possible solutions depending on how one defines "the item with maximum frequency". This solution assumes that the function should return the item that appears most frequently in the list, even if there are multiple items with the same maximum frequency. If the problem statement is intended to require the return of a specific item (e.g., the first item with maximum frequency), then the solution would need to be modified accordingly. 