def nth_nums(nums, n):
    # your code here
    result = []
    for num in nums:
        result.append(num ** n)
    return result