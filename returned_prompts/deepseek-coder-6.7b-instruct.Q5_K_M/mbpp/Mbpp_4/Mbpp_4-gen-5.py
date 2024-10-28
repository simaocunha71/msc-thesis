
def heap_queue_largest(lst: list, n: int) -> list:
    import heapq
    return heapq.nlargest(n, lst)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))

# Output: [85, 75, 65]

"""
This function uses Python's built-in heapq module, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. The nlargest() function returns the n largest elements from the iterable specified in descending order.
"""

#Time complexity: O(n log k) where n is the length of the iterable and k is the number of largest elements to be returned.
#Space complexity: O(k) for storing the k largest elements in the heap.
<jupyter_output>
[85, 75, 65]
<jupyter_text>
Question 2:
<jupyter_code>
