```
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count
```
In this function, we are using a nested loop to iterate over the list and check for each pair of elements if their sum is equal to the given sum. If it is, we increment the count. At the end, we return the count of pairs. This solution has a time complexity of O(n^2) where n is the length of the list. It might be slow for very large lists. If you need a more efficient solution, you could use a hash map to store the elements you have seen so far and their counts. This would reduce the time complexity to O(n). 

For example, if you want to count the number of pairs whose sum is equal to 2 and you have the list [1,1,1,1], you would get 6 pairs. The pairs are (1,1), (1,1), (1,1), (1,1), (1,1), (1,1). 

The unit test `assert get_pairs_count([1,1,1,1],2) == 6` ensures that the function works correctly for this specific case. 

This function can be further improved by using a dictionary to store the counts of elements in the list. This would reduce the time complexity to O(n) and make the function more efficient for large lists. 

Here is the improved version of the function:

```
def get_pairs_count(lst, sum):
    count = 0
    counts = {}
    for num in lst:
        if sum - num in counts:
            count += counts[sum - num]
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return count
```

This function works by iterating over the list and for each element, it checks if the difference between the sum and the current element is in the dictionary. If it is, it increments the count by the count of the difference. Then it increments the count of the current element in the dictionary. At the end, it returns the count of pairs. This function has a time complexity of O(n) and is more efficient than the previous version. 