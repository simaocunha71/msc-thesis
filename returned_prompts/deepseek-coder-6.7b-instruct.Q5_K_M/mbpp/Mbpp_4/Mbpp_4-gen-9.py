
def heap_queue_largest(nums, n):
    # Convert the list into a heap
    heapq.heapify(nums)
    # Use nlargest to get the n largest elements
    largest_nums = heapq.nlargest(n, nums)
    # Return in descending order
    return sorted(largest_nums, reverse=True)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))

"""
Explanation:
This program first uses heapq.heapify to convert the list into a heap. This is important because the nlargest function, which we will use to get the n largest elements, assumes that the input is a heap. Then it uses heapq.nlargest to get the n largest elements from the heap. These elements are then sorted in descending order and returned. 
"""
<jupyter_output>
[85, 75, 65]
<jupyter_text>
2. Write a Python function to return the kth smallest number in a list.
<jupyter_code>
