def mul_even_odd(nums: list) -> int:
    even = 1
    odd = 1
    for num in nums:
        if num % 2 == 0:
            even *= num
        else:
            odd *= num
    return even * odd

