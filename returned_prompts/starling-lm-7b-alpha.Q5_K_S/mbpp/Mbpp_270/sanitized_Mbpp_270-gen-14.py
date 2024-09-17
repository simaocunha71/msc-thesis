def sum_even_and_even_index(nums):
    even_sum = 0
    for i, num in enumerate(nums):
        if i % 2 == 0 and num % 2 == 0:
            even_sum += num
    return even_sum