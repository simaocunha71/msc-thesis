
def find_remainder(arr, n):
    product = 1
    for i in arr:
        product = (product * i) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11))  # Output: 9

Explanation:
The function find_remainder takes an array and an integer n as arguments. It initializes a variable product to 1. Then it iterates through each number i in the array and multiplies product by i modulo n. The result is the product of all numbers in the array modulo n. This is calculated using the modulo operation %, which returns the remainder of the division of the first number by the second.

The product of the numbers in the array [ 100, 10, 5, 25, 35, 14 ] modulo 11 is 9, so the function returns 9.
"""
