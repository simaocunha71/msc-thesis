```
import heapq
def heap_queue_largest(lst,n):
    return heapq.nlargest(n, lst)
```
This function uses the built-in `heapq.nlargest` function to find the n largest integers from the given list of numbers. The `heapq.nlargest` function returns the n largest elements from the iterable specified by the input list, in descending order.

For example, if we call `heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3)`, it will return `[85, 75, 65]`, which are the 3 largest integers from the input list. The function is efficient because it uses a heap data structure, which allows it to find the n largest elements in O(n log k) time, where k is the number of largest elements to find.

The unit test `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]` ensures that the function returns the correct result for the given input. The function is also tested with other inputs to ensure it works correctly for different lists and values of n.