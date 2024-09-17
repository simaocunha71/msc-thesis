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
This function works by first creating a dictionary where the keys are the items in the list and the values are the frequencies of those items. It then returns the key with the maximum value, which is the item with the maximum frequency. 

For example, if the input list is [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2], the function will return 2, which is the item with the maximum frequency in the list. 

The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` ensures that the function works correctly. 

This function assumes that the list is not empty and that there is at least one item in the list with the maximum frequency. If the list is empty or there is no item with the maximum frequency, the function will raise a KeyError. 

If you want to handle these cases, you can add error checking code to the function. For example, you could return a default value or raise a custom exception if the list is empty or there is no item with the maximum frequency. 