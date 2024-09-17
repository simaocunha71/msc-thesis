```
def freq_count(lst):
    freq = {}
    for element in set(lst):
        freq[element] = lst.count(element)
    return freq
```


The provided unit test `assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})` suggests that the function should return a dictionary where the keys are the elements in the list and the values are their respective frequencies. The function `freq_count` iterates over the unique elements in the list (using a set to eliminate duplicates) and counts the frequency of each element using the `count` method. The result is a dictionary where each key-value pair corresponds to an element and its frequency in the list.  The function returns this dictionary.  



For example, if the input list is `[10,10,10,10,20,20,20,20,40,40,50,50,30]`, the function will return `{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}`, which is the desired output.  



This solution has a time complexity of O(n^2) due to the use of the `count` method, which iterates over the entire list for each unique element. However, this is acceptable for small to medium-sized input lists. For larger lists, a more efficient solution using a dictionary or a collections.Counter object would be necessary.  



Here's an alternative solution using a dictionary and the `collections.Counter` class:

```
from collections import Counter

def freq_count(lst):
    return dict(Counter(lst))
```

This solution has a time complexity of O(n) and is more efficient for larger input lists.  



Both of these solutions will pass the provided unit test.  



It's worth noting that the original problem statement doesn't specify whether the output dictionary should include elements with a frequency of 0. In this solution, elements with a frequency of 0 are not included in the output dictionary. If you want to include elements with a frequency of 0, you can modify the solution to use a dictionary comprehension:

```
def freq_count(lst):
    return {element: lst.count(element) for element in set(lst)}
```

This solution will include elements with a frequency of