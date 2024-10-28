def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize rolling_max list with None
    rolling_max = [None] * len(numbers)
    # Initialize max_num with first element in the list
    max_num = numbers[0]
    # Initialize max_index with zero
    max_index = 0
    # Iterate over the list from the second element to the last
    for i in range(1, len(numbers)):
        # If the current element in the iteration is greater than max_num then
        if numbers[i] > max_num:
            # Set max_num to the current element and set max_index to the index of the current element
            max_num = numbers[i]
            max_index = i
        # If the current element is not greater than max_num then
        else:
            # Add the max_num to the rolling_max list at the index of the current element
            rolling_max[i] = max_num
    # If the current element is greater than max_num then
    if numbers[-1] > max_num:
        # Set max_num to the last element of the list
        max_num = numbers[-1]
    # Add the max_num to the rolling_max list at the last index of the list
    rolling_max[-1] = max_num
    # Return the rolling_max list
    return rolling_max


# Test
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))





# This code is contributed by Siddharth






def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize rolling_max list with None
    rolling_max = [None] * len(numbers)
    # Initialize max_num with first element in the list
    max_num = numbers[0]
    # Initialize max_index with zero
    max_index = 0
    # Iterate over the list from the second element to the last
    for i in range(1, len(numbers)):
        # If the current element in the iteration is greater than max_num