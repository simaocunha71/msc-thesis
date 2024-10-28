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


In this function, we iterate over each item in the list. If the item is already in the dictionary, we increment its count by 1. If the item is not in the dictionary, we add it with a count of 1. Finally, we return the dictionary. The unit test provided ensures that the function works correctly. 

For example, if we call `freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])`, the function will return `{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}`, which is the correct frequency count for the input list. 





