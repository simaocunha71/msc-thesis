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


This function iterates over each list in the input list of lists. For each list, it iterates over each item in the list. If the item is already in the frequency dictionary, it increments the count by 1. If the item is not in the dictionary, it adds the item with a count of 1. The function then returns the frequency dictionary.

The unit test provided ensures that the function works correctly:
```
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
```


This test case checks that the function correctly counts the frequency of each item in the flattened list of lists. The expected output is a dictionary with the item as the key and the frequency as the value. The test case checks that the function returns the correct output for a specific set of input lists. If the function returns the correct output for this test case, it is likely to work correctly for other input lists as well. 





This is a Python solution, which is the language used in the problem description. The function `frequency_lists` takes a list of lists as an argument and returns a dictionary where the keys are the unique elements in the flattened list of lists and the values are their frequencies. The function uses a dictionary to keep track of the frequency of each element. It iterates over each list in the input list of lists, and for each list, it iterates over each element in the list. If the element is already in the frequency dictionary, it increments the count by 1. If the element is not in the dictionary, it adds the element with a count of 1. The function then returns the frequency dictionary.

The unit test provided ensures that the function works correctly:
```
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8