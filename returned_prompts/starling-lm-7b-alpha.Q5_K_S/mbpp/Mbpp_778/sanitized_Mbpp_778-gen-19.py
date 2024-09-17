def pack_consecutive_duplicates(nums: list) -> list:
    result = []
    curr = []
    for elem in nums:
        if not curr or curr[-1] != elem:
            curr = [elem]
        else:
            curr.append(elem)
        if len(curr) == 2:
            result.append(curr)
            curr = []
    if curr:
        result.append(curr)
    return result