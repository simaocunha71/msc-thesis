```
import heapq
def heap_queue_largest(lst,n):
    return heapq.nlargest(n, lst)
```


The problem is asking to write a function that finds the n largest integers from a given list of numbers and returns them in descending order.

The unit test `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]` suggests that the function should return the n largest numbers from the list in descending order.

The solution uses the `heapq.nlargest` function from Python's `heapq` module, which returns the n largest elements from the iterable specified by the input list. The `nlargest` function is stable and returns the largest n elements from the iterable specified by the input list, maintaining the original order of equal elements.

Here is the solution:
```
import heapq
def heap_queue_largest(lst,n):
    return heapq.nlargest(n, lst)
```
This function takes a list of numbers and an integer n as input, and returns the n largest numbers from the list in descending order. The `heapq.nlargest` function is used to find the n largest elements from the input list, and the result is returned as a list. The function is stable, meaning that if there are equal elements in the list, their original order is preserved.