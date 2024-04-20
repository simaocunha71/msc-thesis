"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""

def heap_queue_largest(numbers, k):
    """Recursive version of the max-heap algorithm using a min-heap,
        returning the k largest numbers.
    """
    # base case: we've run out of elements
    if len(numbers) == 0:
        return []
    heap = [numbers[-1]] + list(reversed(numbers[:-1]))
    while len(heap) > k:
        heap.pop()
    return heap[::-1] # Reverse the order of elements in heap
    
#print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))