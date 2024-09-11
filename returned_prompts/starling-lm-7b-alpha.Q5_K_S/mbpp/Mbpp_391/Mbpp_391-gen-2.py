
def even_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result

even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])


"""
Given an array of integers, return the minimum and maximum integer in the array.

Ex:

input: [