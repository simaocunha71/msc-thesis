
def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

print(armstrong_number(153)) # True
print(armstrong_number(123)) # False

"""
In the above Python code, we first find the total number of digits in the number. Then, we calculate the sum of the digits raised to the power of the total number of digits. If the sum is equal to the original number, then it's an Armstrong number.
"""

"""
