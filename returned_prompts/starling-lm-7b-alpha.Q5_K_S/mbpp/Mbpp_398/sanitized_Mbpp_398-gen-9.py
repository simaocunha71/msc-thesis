def sum_of_digits(nums):
    total=0
    for num in nums:
        total+=sum(int(i) for i in str(num))
    return total