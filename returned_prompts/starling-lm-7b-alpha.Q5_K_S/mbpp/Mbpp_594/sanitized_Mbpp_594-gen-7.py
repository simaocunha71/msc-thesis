def diff_even_odd(nums):
    even, odd = [], []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even[0] - odd[0] if len(odd) > 0 and len(even) > 0 else None