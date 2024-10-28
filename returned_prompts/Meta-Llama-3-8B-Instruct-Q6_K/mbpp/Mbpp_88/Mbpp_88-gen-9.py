```
def freq_count(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
```


This function iterates over each item in the list. If the item is already in the frequency dictionary, it increments the count by 1. If the item is not in the dictionary, it adds the item with a count of 1. The function returns the frequency dictionary. 

The unit test `assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})` ensures that the function works correctly. It checks if the frequency count for the given list is equal to the expected frequency count. If the function works correctly, this assertion will not raise an error. 

This function has a time complexity of O(n), where n is the number of items in the list, because it iterates over each item in the list once. It has a space complexity of O(n) as well, because in the worst case, it needs to store each item in the frequency dictionary. 





