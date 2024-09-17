def unique_sublists(nums: list) -> dict:
    return {tuple(sublist): sublist.count(tuple(sublist)) for sublist in nums}

