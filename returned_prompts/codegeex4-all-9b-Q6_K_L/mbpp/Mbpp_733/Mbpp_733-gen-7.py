def find_first_occurrence(nums: list, n: int) -> int:
    for i, num in enumerate(nums):
        if num == n:
            return i
    return -1

