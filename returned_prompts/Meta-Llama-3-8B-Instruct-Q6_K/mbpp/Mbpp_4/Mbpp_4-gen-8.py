```
import heapq

def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```
This problem can be solved by using the heapq module in Python, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. The function `heapq.nlargest(n, lst)` returns the n largest elements from the iterable specified by lst.

The unit test provided, `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]`, shows that the function should return the 3 largest integers from the given list, in descending order.

Here's how the function works:

1. The function takes two parameters: `lst`, the list of numbers, and `n`, the number of largest integers to return.
2. The function uses the `heapq.nlargest(n, lst)` function to find the `n` largest elements in the list.
3. The function returns the `n` largest elements in descending order.

This solution has a time complexity of O(n log k), where n is the length of the input list and k is the number of largest elements to return. This is because the `heapq.nlargest` function uses a heap data structure to store the `n` largest elements, and the heap operations (insertion and extraction of the maximum element) take O(log k) time. The function iterates over the input list once, so the overall time complexity is O(n log k). The space complexity is O(k), as the function stores the `n` largest elements in the heap.