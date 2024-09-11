"""
To solve this problem, you can use the heap_sort method from the heapq module in Python. Here's an example of how you can use it:

1. Import the heapq module.
2. Define the heap_sort function that takes a list as input.
3. Use the heapify function from the heapq module to create a max-heap from the input list.
4. Use the heappop function from the heapq module to remove the maximum element from the heap and append it to a new list called sorted_list.
5. Repeat step 4 until the heap is empty.
6. Return the sorted_list.

Here's the code for the heap_sort function:

import heapq

def heap_sort(lst):
    """Sort a list using heap sort."""
    heapq.heapify(lst)
    sorted_list = []
    while lst:
        sorted_list.append(heapq.heappop(lst))
    return sorted_list

You can use the assert statement to verify that the heap_sort function works correctly. The assert statement checks if the result of the heap_sort function is equal to the expected result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. If the assertion is true, the program will continue execution. Otherwise, an AssertionError will be raised.
"""
import heapq

def heap_sort(lst):
    """Sort a list using heap sort."""
    heapq.heapify(lst)
    sorted_list = []
    while lst:
        sorted_list.append(heapq.heappop(lst))
    return sorted_list

assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Output: True

"""

In this example, the assert statement checks if the result of the heap_sort function with the input [1, 3, 5, 7, 9, 2, 4, 6, 8