```
def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for item in lst:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
    return frequency
```


This function works by iterating over each list in the input list of lists. For each list, it iterates over each item in the list. If the item is already a key in the frequency dictionary, it increments the value by 1. If the item is not a key in the frequency dictionary, it adds the item as a key with a value of 1. The function then returns the frequency dictionary. The unit test provided shows that this function works correctly. For example, the test case `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` ensures that the function correctly counts the frequency of each item in the input lists.