```
def maximum(arr, k):
    return sorted(set(arr))[-k:]
```



Explanation:
1. `set(arr)` is used to remove duplicate elements from the array.
2. `sorted()` is used to sort the array in ascending order.
3. `[-k:]` is used to return the last `k` elements of the sorted array, which are the maximum `k` numbers in the array.

For example, if the input array is `[-3, -4, 5]` and `k` is `3`, the output will be `[-4, -3, 5]`, which are the maximum `3` numbers in the array.

This solution has a time complexity of O(n log n) due to the sorting operation, where `n` is the length of the array. The space complexity is O(n) due to the use of the `set` data structure to remove duplicates.