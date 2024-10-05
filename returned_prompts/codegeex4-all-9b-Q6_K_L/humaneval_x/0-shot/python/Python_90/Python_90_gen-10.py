def next_smallest(lst):
    if len(lst) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest

print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None