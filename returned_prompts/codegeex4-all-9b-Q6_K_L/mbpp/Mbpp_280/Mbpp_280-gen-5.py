def sequential_search(nums: list, el: int):
    for i, num in enumerate(nums):
        if num == el:
            return (True, i)
    return (False, -1)