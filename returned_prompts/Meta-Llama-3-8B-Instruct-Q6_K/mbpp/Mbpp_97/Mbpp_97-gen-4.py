```
def frequency_lists(lists):
    freq_dict = {}
    for lst in lists:
        for num in lst:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
    return freq_dict
```


This function works by iterating over each list in the input list of lists. For each list, it iterates over each number in the list. If the number is already in the frequency dictionary, it increments the count for that number. If the number is not in the dictionary, it adds it with a count of 1. Finally, it returns the frequency dictionary. The unit test provided ensures that the function works correctly. For example, the test `assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}` checks that the function returns the correct frequency dictionary for the given input. 





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





```
def frequency_lists(lists):
    frequency = {}
    for lst in lists:
        for num in lst:
            frequency[num] = frequency.get(num, 0) + 1
    return frequency
```





```
from collections import Counter

def frequency_lists(lists):
    frequency = Counter(num for lst in lists for num in lst)
    return dict(frequency)
```





```
from collections import Counter

def frequency_lists(lists):
    return dict(Counter(num for lst in lists for num in lst))
```





```
from collections import Counter

def frequency_lists(lists):
    return dict(Counter([num for lst in lists for num in lst]))
```





```
from collections import Counter

def frequency_lists(lists):
    return dict(Counter([i for lst in lists for i in lst]))
```





```
from collections import Counter

def frequency_lists(lists):
    return dict(Counter([i for lst in