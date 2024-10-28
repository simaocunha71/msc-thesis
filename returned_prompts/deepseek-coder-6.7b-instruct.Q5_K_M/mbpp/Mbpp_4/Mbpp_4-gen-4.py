
def heap_queue_largest(num_list, n):
    import heapq
    return heapq.nlargest(n, num_list)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58],3))

# Output: [85, 75, 65]

This function uses the heapq.nlargest method, which returns the n largest elements from the iterable in descending order.

Alternatively, if you don't want to use any built-in functions, you can manually implement this by creating a max heap and popping the elements off until you've retrieved the n largest numbers. This can be quite complex and is usually not the best approach unless you have a specific reason to avoid using built-in functions.
"""

