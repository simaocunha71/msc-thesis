```
def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]
```
Explanation:
The function `maximum` takes two parameters: `arr` (a list of integers) and `k` (a positive integer). It returns a sorted list of length `k` with the maximum `k` numbers in `arr`.

The solution uses the built-in `sorted` function to sort the input list `arr` in descending order (i.e., in reverse). This is done by passing the `reverse=True` argument to `sorted`. The sorted list is then sliced to extract the first `k` elements, which are the maximum `k` numbers in the original list.

For example, if `arr = [-3, -4, 5]` and `k = 3`, the function will return `[-4, -3, 5]`, which are the three largest numbers in the input list.

This solution has a time complexity of O(n log n) due to the sorting operation, where `n` is the length of the input list. The space complexity is O(k) because we need to store the result list of length `k`. A more efficient solution could be achieved using a heap data structure, but this would require a more complex implementation.