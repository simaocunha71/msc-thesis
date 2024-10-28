def pack_consecutive_duplicates(nums:list) -> list:
    result = []
    cur = []
    for n in nums:
        cur.append(n)
        if not cur or cur[-1] != n:
            result.append(list(cur))
            cur = []
    return result