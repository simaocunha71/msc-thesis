def mul_even_odd(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    odd_nums = [num for num in lst if num % 2 != 0]
    
    if not even_nums:
        return 0
    if not odd_nums:
        return 0
    
    return even_nums[0] * odd_nums[0]