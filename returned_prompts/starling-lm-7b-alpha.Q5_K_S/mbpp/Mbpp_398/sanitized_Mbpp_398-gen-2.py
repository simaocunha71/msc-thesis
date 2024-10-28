def sum_of_digits(nums):
    result = 0
    for num in nums:
        result += sum(int(i) for i in str(num))
    return result