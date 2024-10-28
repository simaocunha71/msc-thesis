```
import heapq

def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```
The problem is asking for a function that takes a list of numbers and returns the n largest integers from that list in descending order. 

The unit test `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]` suggests that the function should return the top n elements from the list, in descending order.

This can be solved using the heapq module in Python, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. The `heapq.nlargest(n, lst)` function returns the n largest elements from the list `lst`, in descending order.

Here is the solution:
```
import heapq

def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```
This function takes a list `lst` and an integer `n` as input, and returns the n largest elements from the list in descending order. The `heapq.nlargest(n, lst)` function does the heavy lifting, and the function simply returns the result. 