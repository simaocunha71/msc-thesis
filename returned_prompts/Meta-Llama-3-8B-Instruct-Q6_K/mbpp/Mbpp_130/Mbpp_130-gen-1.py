```
def max_occurrences(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return max(freq, key=freq.get)
```


This function works by creating a dictionary, `freq`, where the keys are the items in the list and the values are their frequencies. It then uses the `max` function with a `key` argument to find the item with the maximum frequency. The `key` argument tells the `max` function to use the values in the dictionary (i.e., the frequencies) to determine the maximum. The `max` function returns the key (i.e., the item) with the maximum value (i.e., the frequency). If there are multiple items with the same maximum frequency, this function will return one of them arbitrarily. The unit test provided ensures that this function works correctly. For example, the test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` checks that the function returns `2`, which is the item with the maximum frequency in the list.