def square_nums(nums: list) -> list:
    return [num ** 2 for num in nums]  # using list comprehension
    # or
    # result = []
    # for num in nums:
    #     result.append(num ** 2)
    # return result  # using for loop
    # or
    # return list(map(lambda x: x ** 2, nums))  # using map function with lambda function
    # or
    # return [pow(num, 2) for num in nums]  # using pow function