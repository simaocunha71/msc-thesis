def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum + 1):
        if all(i % int(digit) == 0 for digit in str(i) if digit != '0'):
            result.append(i)
    return result

print(divisible_by_digits(1,22))

#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


Explanation:
The function divisible_by_digits accepts two arguments, startnum and endnum. The function then generates a list of numbers within the range from startnum to endnum. For each number in this range, it checks if the number is divisible by every digit it contains. This is done by converting the number to a string and iterating over its digits. The function uses the all function and the generator expression to check if all digits are divisors of the number. If the number passes this check, it is appended to the result list. The function returns the result list.
"""

#Example 2:
