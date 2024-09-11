def square_nums(nums):
    return [n ** 2 for n in nums]  # list comprehension to square each number in the list
    # or
    # return [num**2 for num in nums]  # same as above
    # or
    # result = []
    # for num in nums:
    #     result.append(num ** 2)
    # return result  # same as above