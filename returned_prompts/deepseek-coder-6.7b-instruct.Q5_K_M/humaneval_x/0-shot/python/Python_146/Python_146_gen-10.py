
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            strNum = str(abs(num))
            if strNum[0] in '13579' and strNum[-1] in '13579':
                count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2
print(specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 0
print(specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 100]))  # 10
print(specialFilter([-11, -22, -33, -44, -55, -66, -77, -88, -99, -100]))  # 0

This Python function works by iterating over the input list of numbers, converting each to a string, and checking if the first and last digits are odd (i.e., '1', '3', '5', '7', or '9'). If both conditions are met, it increments a counter. At the end of the function, it returns the count of numbers that met the criteria.
'''

# Q2:
'''
