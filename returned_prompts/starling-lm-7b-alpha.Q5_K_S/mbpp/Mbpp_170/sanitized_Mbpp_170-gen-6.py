def sum_range_list(numbers, start_index, end_index):
    # Check if the indices are valid
    if start_index < 0 or end_index > len(numbers) - 1:
        raise ValueError("Index out of range")
    # Calculate the sum of the numbers within the range
    total = sum(numbers[start_index: end_index+1])
    # Return the sum
    return total
numbers = [2,1,5,6,8,3,4,9,10,11,8,12]
start_index = 8
end_index = 10