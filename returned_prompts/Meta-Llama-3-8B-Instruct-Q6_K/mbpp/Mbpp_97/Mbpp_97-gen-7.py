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


In this function, we initialize an empty dictionary `frequency_dict` to store the frequency of each element. We then iterate over each list in the input list of lists. For each list, we iterate over each element in the list. If the element is already in the dictionary, we increment its frequency by 1. If the element is not in the dictionary, we add it with a frequency of 1. Finally, we return the `frequency_dict`. 

The unit test `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` confirms that the function works correctly. 
```python
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
```


This function works by iterating over each list in the input list of lists, and then iterating over each element in each list. It uses a dictionary to keep track of the frequency of each element. The time complexity is O(n), where n is the total number of elements in the input list of lists. The space complexity is also O(n), as in the worst case, we might have to store each element in the dictionary. 
```python
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


This function is also known as