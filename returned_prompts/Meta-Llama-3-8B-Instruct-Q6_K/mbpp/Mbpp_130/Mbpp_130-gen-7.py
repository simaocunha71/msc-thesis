```
def max_occurrences(lst):
    from collections import Counter
    counter = Counter(lst)
    max_freq = max(counter.values())
    max_items = [item for item, freq in counter.items() if freq == max_freq]
    return max_items[0]
```
This function works by first counting the occurrences of each item in the list using the Counter class from the collections module. It then finds the maximum frequency by taking the maximum of the values in the counter. Finally, it finds the items with the maximum frequency by creating a list of items that have the maximum frequency, and returns the first one (since it's a list, it doesn't matter which one is returned).

The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2` ensures that the function returns the correct item when there are multiple items with the maximum frequency. In this case, the function returns 2, which is the correct answer.