    numbers.sort()
    smallest_difference = float('inf')
    closest_pair = ()
    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < smallest_difference:
            smallest_difference = difference
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair


if __name__ == "__main__":
    import doctest
    doctest.testmod()

This script first sorts the list of numbers. It then iterates through the sorted list to find the smallest difference between each pair of consecutive numbers. The pair of numbers that result in the smallest difference are then returned.
"""

#Task 2

"""
