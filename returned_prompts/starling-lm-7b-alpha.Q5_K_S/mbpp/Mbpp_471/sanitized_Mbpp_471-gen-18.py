def find_remainder(nums: list, mod: int) -> int:
    if mod == 1:
        return 0
    if mod == 0:
        return None
    product = 1
    for num in nums:
        product *= num % mod
    return product % mod