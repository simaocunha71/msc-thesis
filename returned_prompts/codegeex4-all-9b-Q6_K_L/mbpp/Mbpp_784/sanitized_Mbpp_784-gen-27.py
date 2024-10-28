def mul_even_odd(nums: list) -> int:
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even[0]*odd[0]