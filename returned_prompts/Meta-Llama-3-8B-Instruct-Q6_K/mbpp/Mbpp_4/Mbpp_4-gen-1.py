```
import heapq
def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```


The unit test `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]` helps in understanding the expected output. It is clear that the function should return the `n` largest integers from the given list, in descending order. 

The problem can be solved by using the `heapq.nlargest` function in Python, which returns the `n` largest elements from the iterable specified. The iterable can be a list, tuple, dictionary, or any other type that supports iteration. The function `heap_queue_largest` takes two parameters: `lst` (the list of numbers) and `n` (the number of largest integers to return). It returns a list of the `n` largest integers from `lst`, in descending order.

Here is the Python code that solves the problem:
```
import heapq
def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```
This code uses the `heapq.nlargest` function to find the `n` largest integers from the list `lst`. The result is a list of the `n` largest integers, in descending order. The unit test `assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]` ensures that the function returns the correct result.