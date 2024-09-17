def find_first_occurrence(nums: list, target: int) -> int:
    # Initialize result
    result = -1

    # Find the first occurrence
    for i in range(len(nums)):
        if nums[i] == target:
            result = i
            break

    return result