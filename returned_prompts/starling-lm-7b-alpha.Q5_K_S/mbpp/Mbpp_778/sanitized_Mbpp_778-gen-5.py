def pack_consecutive_duplicates(nums):
    result = []
    cur = []
    for i in nums:
        if not cur or cur[-1] != i:
            cur = [i]
        else:
            cur.append(i)
        if len(cur) >= 2:
            result.append(cur)
            cur = [i]
    if cur:
        result.append(cur)
    return result