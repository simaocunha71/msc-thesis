```
def kth_element(arr, k):
    return arr[k-1]
```
The problem asks to find the kth element in a given array using 1-based indexing. The unit test `assert kth_element([12,3,5,7,19], 2) == 3` suggests that the indexing is 1-based, meaning the first element is at index 1, not 0.

The solution is straightforward. Since the indexing is 1-based, we simply subtract 1 from the given index k to get the correct 0-based index. Then, we return the element at that index in the array. This works because in Python, list indices start at 0. For example, the first element in the array is at index 0, the second element is at index 1, and so on. So, to get the kth element, we need to subtract 1 from k to get the correct 0-based index.