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


The problem is asking you to create a function that finds the item with the maximum frequency in a given list. 

The provided unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` helps clarify the problem by showing that the function should return the item with the maximum frequency, not the frequency itself.

Here is a Python solution for the problem:

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

This function works by first creating an empty dictionary `freq`. Then, it iterates over each item in the list. If the item is already in the dictionary, it increments the count by 1; otherwise, it adds the item to the dictionary with a count of 1. Finally, it returns the item with the maximum frequency by using the `max` function with a key function that returns the frequency of each item. The `max` function returns the item with the maximum frequency. 

This solution has a time complexity of O(n), where n is the length of the list, because it iterates over the list once. The space complexity is also O(n) because in the worst case, all items in the list are unique and the dictionary will contain n items. 