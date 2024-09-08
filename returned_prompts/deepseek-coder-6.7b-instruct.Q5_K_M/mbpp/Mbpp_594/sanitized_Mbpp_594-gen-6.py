def diff_even_odd(nums):
    even_num = next((num for num in nums if num % 2 == 0), None)
    odd_num = next((num for num in nums if num % 2 != 0), None)
    return even_num - odd_num if even_num and odd_num else None