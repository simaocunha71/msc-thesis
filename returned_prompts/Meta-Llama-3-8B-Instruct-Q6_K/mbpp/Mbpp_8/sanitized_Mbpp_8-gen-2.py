def square_nums(nums):
    return [num ** 2 for num in nums]  # List comprehension to square each number in the list
    # or
    # return list(map(lambda x: x ** 2, nums))  # Using map function to square each number in the list
    # or
    # result = []
    # for num in nums:
    #     result.append(num ** 2)
    # return result  # Using for loop to square each number in the list
    # The above three ways can be used to solve the problem. The first one is most common and efficient.