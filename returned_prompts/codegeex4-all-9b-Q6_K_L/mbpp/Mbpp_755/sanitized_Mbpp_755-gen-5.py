def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    smallest = second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        raise ValueError("List does not contain a second distinct smallest element")
    return second_smallest