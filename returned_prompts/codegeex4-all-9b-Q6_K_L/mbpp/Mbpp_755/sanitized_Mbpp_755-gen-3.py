def second_smallest(nums):
    if len(nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None