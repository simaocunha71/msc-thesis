"""
The function `heap_queue_largest` uses a min heap to keep track of the largest numbers. It starts by initializing the min heap with the first `n` numbers from the input list. Then it iterates through the rest of the list. For each number, it adds it to the heap, and if the heap becomes larger than `n`, it removes the smallest number.

The function `min_heapify` is a helper function for `heap_queue_largest`. It rearranges the min heap to make sure the smallest element is at the root. It does this by swapping the root with the smallest child, and then sifting up or sifting down until the heap is restored.
"""

def heap_queue_largest(nums, n):
    """
    Returns the n largest numbers from `nums` in descending order.

    Time complexity: O(n log n)
    """
    # Create a min heap with the first n numbers from nums
    min_heap = [(nums[i], i) for i in range(n)]
    heapq.heapify(min_heap)

    # Add each of the remaining numbers to the heap, removing the smallest number if necessary
    for num in nums[n:]:
        heapq.heappush(min_heap, (num, -i))
        if len(min_heap) > n:
            heapq.heappop(min_heap)

    # Extract the n largest numbers from the heap and return them
    return [num for _, num in min_heap]


def min_heapify(heap, i):
    """
    Re-arranges the heap such that the smallest element is at the root.

    Time complexity: O(log n)
    """
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    # Find the smallest child
    if left < len(heap) and heap[left][0] < heap[i][0]:
        smallest = left
    if right < len(heap) and heap[right][0] < heap[smallest][0]:
        smallest = right

    # Swap the root with the smallest child and re-