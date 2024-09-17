
def pack_consecutive_duplicates(nums: list) -> list:
    result = []
    current = []
    for i in nums:
        if not current or current[-1] != i:
            current = [i]
        else:
            current.append(i)
        if len(current) == 2:
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result


