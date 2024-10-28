
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            if str(num)[0] in '13579' and str(num)[-1] in '13579':
                count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2
print(specialFilter([1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))  # 6
print(specialFilter([20, 21, 22, 23, 24, 25, 26, 27, 28, 29]))  # 0
print(specialFilter([10, 100, 1000, 10000, 100000]))  # 0
print(specialFilter([-10, -11, -12, -13, -14, -15, -16, -17, -18, -19]))  # 0


The function specialFilter first initializes a counter to zero. Then it iterates over each number in the input array. If the number is greater than 10 and its first and last digits are odd, it increments the counter. Finally, it returns the counter.
The function str(num)[0] gets the first character of the string representation of the number and str(num)[-1] gets the last character. The in operator in Python checks if a character is in a string. In this case, it checks if the first and last characters are in the string '13579', which are the odd digits.
"""

# 6. 
"""
