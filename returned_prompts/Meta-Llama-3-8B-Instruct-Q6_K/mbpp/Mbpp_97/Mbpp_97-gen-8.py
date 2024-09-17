```
def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for num in lst:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    return frequency
```
The function `frequency_lists` takes a list of lists as input and returns a dictionary where the keys are the elements from the flattened list of lists and the values are their frequencies.

The function iterates over each list in the input list of lists, and then over each element in each list. If the element is already in the `frequency` dictionary, its count is incremented by 1. If the element is not in the `frequency` dictionary, it is added with a count of 1.

The unit test `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` confirms that the function works correctly. It checks that the output of `frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])` is `{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}`, which is the expected output. 