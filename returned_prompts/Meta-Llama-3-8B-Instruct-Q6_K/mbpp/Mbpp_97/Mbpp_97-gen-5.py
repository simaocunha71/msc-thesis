```
def frequency_lists(lists):
    frequency_dict = {}
    for lst in lists:
        for element in lst:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict
```


This function iterates over each list in the input list of lists, and then iterates over each element in the list. For each element, it checks if the element is already in the frequency dictionary. If it is, it increments the count by 1. If it's not, it adds the element to the dictionary with a count of 1. Finally, it returns the frequency dictionary. The unit test provided ensures that the function works correctly. 

For example, the unit test `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` checks that the function correctly counts the frequency of each element in the flattened list of lists. 





