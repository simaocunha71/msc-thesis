```
def consecutive_duplicates(lst):
    if len(lst) == 0:
        return []
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            result.append(lst[i])
    return result
```


This function iterates through the list, adding each element to the result list only if it is different from the previous element. This effectively removes consecutive duplicates from the list. The function also handles the case where the input list is empty, in which case it returns an empty list. 

The unit test provided, `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`, ensures that the function works correctly by checking that the output of the function on a specific input is equal to the expected output. 

Note: This function does not preserve the original order of elements, it only removes consecutive duplicates. If you want to preserve the order and remove all duplicates (not just consecutive ones), you would need a different approach. 

For example, you could use a dictionary to keep track of unique elements, and then convert the dictionary back to a list. This would also preserve the original order of elements. 

Here's an example of how you could do that:

```
def unique_elements(lst):
    seen = {}
    result = []
    for element in lst:
        if element not in seen:
            seen[element] = True
            result.append(element)
    return result
```

This function uses a dictionary to keep track of unique elements, and then converts the dictionary back to a list. It also preserves the original order of elements, as it iterates through the input list in the same order. 

However, this function does not remove consecutive duplicates, it removes all duplicates. If you want to remove consecutive duplicates and preserve the original order, you would need to use a different approach, such as the one shown in the original function. 

It's worth noting that the problem statement is not entirely clear, and it's not specified whether the function should remove all duplicates or just consecutive duplicates. The unit test provided suggests that the function should remove consecutive duplicates, but preserve the