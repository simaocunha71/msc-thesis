    # Get the index of the smallest and largest numbers in the list
    smallest_number_index = numbers.index(min(numbers))
    largest_number_index = numbers.index(max(numbers))

    # Return the two numbers in the correct order
    return (
        numbers[smallest_number_index],
        numbers[largest_number_index],
    )
