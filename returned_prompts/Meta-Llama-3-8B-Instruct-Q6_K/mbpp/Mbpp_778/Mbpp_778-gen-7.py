```
def pack_consecutive_duplicates(lst):
    result = []
    current = []
    for i in lst:
        if not current or i != current[-1]:
            if current:
                result.append(current)
            current = [i]
        else:
            current.append(i)
    if current:
        result.append(current)
    return result
```

The function `pack_consecutive_duplicates` takes a list as input and returns a new list where consecutive duplicates of elements are packed into sublists. 

The function iterates over the input list. For each element, it checks if the current element is the same as the last element in the current sublist. If not, it adds the current sublist to the result list and starts a new sublist with the current element. If the current element is the same as the last element in the current sublist, it adds the current element to the current sublist. 

After iterating over the entire list, the function adds the last sublist to the result list if it is not empty. 

The function then returns the result list. 

The unit test `assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]` ensures that the function works correctly. 

This function has a time complexity of O(n), where n is the length of the input list, because it iterates over the list once. The space complexity is also O(n), because in the worst case, the function may need to store all elements of the input list in the result list. 