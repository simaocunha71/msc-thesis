def heap_queue_largest(nums, n):
    # Convert the list into a heap
    heapq.heapify(nums)
    # Use nlargest to get the n largest elements
    largest_nums = heapq.nlargest(n, nums)
    # Return in descending order
    return sorted(largest_nums, reverse=True)