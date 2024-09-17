```
def get_pairs_count(lst, sum):
    pairs_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                pairs_count += 1
    return pairs_count
```


This function will return the number of pairs in the list that sum up to the given sum. It does this by iterating over the list and checking each pair of elements to see if they sum up to the given sum. If they do, it increments a counter. Finally, it returns the counter.

The unit test `assert get_pairs_count([1,1,1,1],2) == 6` suggests that the function should count the number of pairs in the list that sum up to the given sum. In this case, the list is [1,1,1,1] and the sum is 2. The function should return 6, which is the number of pairs in the list that sum up to 2.

This function has a time complexity of O(n^2) because it uses two nested loops to iterate over the list. This means it will be less efficient for large lists. If you need to count the number of pairs in a large list, you may want to consider using a more efficient algorithm or data structure.