def diff_even_odd(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0 or len(odd) == 0:
        return 0
    else:
        return even[0] - odd[0]