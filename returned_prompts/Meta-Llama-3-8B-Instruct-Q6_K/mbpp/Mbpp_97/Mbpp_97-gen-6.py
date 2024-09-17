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


The function `frequency_lists` takes a list of lists as an input and returns a dictionary where the keys are the elements from the list and the values are their frequencies. It iterates over each list in the input list, then over each element in the list. If the element is already in the dictionary, it increments the count by 1, otherwise it adds the element to the dictionary with a count of 1. The function returns the dictionary. 

For example, for the input `[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]`, the function will return `{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}`. The unit test `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` ensures that the function returns the expected result. 












