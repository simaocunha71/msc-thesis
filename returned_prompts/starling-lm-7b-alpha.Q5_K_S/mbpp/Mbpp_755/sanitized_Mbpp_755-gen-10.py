def second_smallest(numbers):
    smallest, second_smallest = float('inf'), float('inf')
    for i in numbers:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest