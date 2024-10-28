
def heap_queue_largest(nums,n):
    import heapq
    return heapq.nlargest(n,nums)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))

"""
heapq is a Python module that provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. It provides a set of functions to work with heap queues.

The function nlargest(n, iterable) returns the n largest elements from the iterable, in descending order.
"""
<jupyter_output>
[85, 75, 65]
<jupyter_text>
