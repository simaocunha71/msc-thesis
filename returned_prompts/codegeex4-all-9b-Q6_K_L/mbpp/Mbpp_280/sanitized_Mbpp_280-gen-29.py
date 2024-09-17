def sequential_search(nums: list, element: int) -> tuple:
    for i, num in enumerate(nums):
        if num == element:
            return (True, i)
    return (False, -1)