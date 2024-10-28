def by_length(arr):
    # Create a list to store the names of the numbers
    numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # Filter out any numbers that are not between 1 and 9 inclusive
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)

    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]

    # Replace each number with its corresponding name
    result = [numbers[num] for num in reversed_arr]

    return result


# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']