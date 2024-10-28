```
def max_occurrences(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq_item = max(frequency, key=frequency.get)
    return max_freq_item
```
The function `max_occurrences` takes a list `lst` as input and returns the item with the maximum frequency in the list. It works by first creating a dictionary `frequency` where the keys are the items in the list and the values are their frequencies. It then finds the item with the maximum frequency using the `max` function with a custom key function, which returns the frequency of each item. Finally, it returns this item. The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` ensures that the function works correctly.  The maximum frequency item in this list is 2, which is returned by the function.  



