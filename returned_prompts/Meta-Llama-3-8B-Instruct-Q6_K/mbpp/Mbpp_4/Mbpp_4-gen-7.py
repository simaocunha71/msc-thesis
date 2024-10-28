```
import heapq
def heap_queue_largest(lst,n):
    return heapq.nlargest(n, lst)
```



The function heap_queue_largest takes a list of numbers and an integer n as input, and returns the n largest integers from the list in descending order. The heapq.nlargest function from the Python heapq module is used to achieve this. This function returns the n largest elements from the iterable specified by the input list, as a list in descending order. For example, if the input list is [25, 35, 22, 85, 14, 65, 75, 22, 58] and n is 3, the function will return [85, 75, 65]. 

The unit test provided, assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65], ensures that the function works correctly for the given input and returns the expected output. 

This function has a time complexity of O(n log k) where n is the length of the input list and k is the number of largest elements to return. This is because the heapq.nlargest function uses a heap data structure to find the n largest elements, which has a time complexity of O(n log k). 

The space complexity is O(k) as the function returns a list of the n largest elements, which requires additional memory to store the result. 

The heapq.nlargest function is efficient and easy to use, making it a good choice for this problem. It is also a good example of how to use the heapq module in Python to solve a problem that requires finding the n largest elements in a list. 