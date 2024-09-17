```
def freq_count(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict
```


This function iterates over each element in the input list. If the element is already in the dictionary, it increments the count by 1. If the element is not in the dictionary, it adds the element to the dictionary with a count of 1. Finally, it returns the dictionary. The unit test provided ensures the function works correctly.