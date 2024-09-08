
def heap_sort(lst):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]

print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Explanation:
The function heap_sort() first converts the input list into a valid heap. This is done with the heapq.heapify() function. Then, it repeatedly removes and returns the smallest element from the heap, which is done with the heapq.heappop() function. The result is a sorted list.
"""
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<jupyter_text>
Question 2
<jupyter_code>
