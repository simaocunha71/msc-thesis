def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    smallest_difference = numbers[1] - numbers[0]
    closest_elements = (numbers[0], numbers[1])

    for i in range(1, len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < smallest_difference:
            smallest_difference = difference
            closest_elements = (numbers[i], numbers[i + 1])

    return closest_elements

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)


This function sorts the input list of numbers in ascending order. It then iterates through the list to find the pair of numbers that have the smallest difference between them. The function returns this pair as a tuple.

The time complexity of this function is O(n log n) because of the sorting operation, where n is the length of the input list. The space complexity is O(1) as it only uses a constant amount of extra space.

I hope this helps you understand the solution. Let me know if you have any other questions.

"""

# Test cases to validate the solution
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
print(find_closest_elements([5.0, 1.0, 9.0, 3