
from heapq import nlargest

def heap_queue_largest(nums, n):
    return sorted(nlargest(n, nums), reverse=True)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))

"""
Explanation:
The function nlargest() from the heapq module returns the n largest elements from the iterable in descending order. Then, the sorted() function is used to sort the result in descending order. 
The sorted() function is used to sort the list in descending order, which is then returned by the function.
"""
<jupyter_output>
[85, 75, 65]
<jupyter_text>
Problem 2:
<jupyter_code>
