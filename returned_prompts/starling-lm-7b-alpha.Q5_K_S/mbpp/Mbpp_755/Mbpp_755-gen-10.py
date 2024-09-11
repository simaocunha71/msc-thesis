def second_smallest(numbers):
    smallest, second_smallest = float('inf'), float('inf')
    for i in numbers:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest


# assert second_smallest([1, 2, -8, -2, 0, -2])==-2
# assert second_smallest([1, 2, 3, 4, 5, 6])==3


"""
Write a function to find the second smallest number in a list.

Explanation:

The function `second_smallest` takes a list of numbers as input and initializes two variables, `smallest` and `second_smallest`, to positive infinity. It then iterates over each number in the input list. If a number is smaller than the current `smallest` value, it updates `second_smallest` to the previous value of `smallest` and `smallest` to the current number. If a number is not smaller than `smallest` but is smaller than `second_smallest`, it updates `second_smallest` to the current number. After iterating over all the numbers in the list, the function returns the value of `second_smallest`, which is the second smallest number in the list.

The provided unit tests assert