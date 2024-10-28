```
import heapq

def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```
This function uses the built-in `heapq.nlargest` function, which returns the n largest elements from the iterable specified by the input list. The output is a list of the n largest integers from the input list, in descending order. For example, if we call `heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3)`, the function will return `[85, 75, 65]`, which are the three largest integers from the input list. The time complexity of this function is O(n log k), where n is the length of the input list and k is the number of largest elements to be found. The space complexity is O(k), as it needs to store the k largest elements.