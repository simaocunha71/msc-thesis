
def heap_queue_largest(nums, n):
    import heapq
    return heapq.nlargest(n, nums)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))

# Output: [85, 75, 65]

Explanation:

This function uses Python's built-in library function "heapq.nlargest()" to find the "n" largest integers in the given list. The 'n' largest numbers are returned in descending order.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
"""
