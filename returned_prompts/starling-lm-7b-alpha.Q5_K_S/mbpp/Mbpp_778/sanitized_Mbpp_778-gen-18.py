def pack_consecutive_duplicates(nums: list) -> list:
    result = []
    tmp = []
    for i in nums:
        if tmp:
            if tmp[-1] == i:
                tmp.append(i)
            else:
                result.append(tmp)
                tmp = [i]
        else:
            tmp.append(i)
    if tmp:
        result.append(tmp)
    return result