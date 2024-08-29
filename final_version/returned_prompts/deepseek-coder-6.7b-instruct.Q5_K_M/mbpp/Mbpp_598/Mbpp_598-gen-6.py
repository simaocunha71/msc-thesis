
def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

print(armstrong_number(153))  # True

"""
Explanation:

In this function, we first calculate the cube of each digit of the number and add it to a sum. Then we check if the sum is equal to the original number. If it is, the number is an Armstrong number and we return True. If it isn't, the number is not an Armstrong number and we return False.
"""

# Q2

