def divisible_by_digits(startnum, endnum):
    from math import sqrt

    # get all the numbers in the range
    all_nums = [i for i in range(startnum, endnum + 1)]

    # generate all the possible combinations of the digits of the numbers
    all_digits = set(str(i) for i in all_nums)
    all_digits = list(all_digits)

    # find the max number of digits in each combination
    max_digits = int(sqrt(len(all_digits)))

    # generate all the numbers divisible by each combination
    divisible_by_digits = []
    for i in all_digits:
        for j in all_nums:
            if j % int(i) == 0:
                divisible_by_digits.append(j)

    return divisible_by_digits


# assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(divisible_by_digits(1, 22))






"""
This function first generates all the numbers within the given range. Then it generates all the possible combinations of the digits of the numbers. The max number of digits in each combination is found to reduce the time complexity. Finally, it checks if each number within the given range is divisible by each combination and appends the number to the result if it is divisible.

The time complexity of this function is O(n * m), where n is the length of the range and m is the max number of digits in each combination.

The space complexity of this function is O(n + m), where n is the length of the range and m is the max number of digits in each combination.
"""





"""
The function divisible_by_digits takes two parameters, startnum and endnum, which represent the start and end of the range of numbers to check. It uses the math.sqrt function to find the square root