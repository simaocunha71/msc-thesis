def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1)]

print(perfect_perfect_squares(1,30))

# Output: [1, 4, 9, 16, 25]

# Explanation: The square root of 1 is 1, the square root of 30 is 5.477225575051661. 
# So, we start our search at 1 and end at 5. The perfect squares between 1 and 30 are: [1, 4, 9, 16, 25]
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a Python function to check if a given number is a perfect number or not. A perfect number is a positive integer that is equal to the sum of its proper positive divisors excluding the number itself. For example, 6 is a perfect number because 1, 2, and 3 are its proper positive divisors and 1 + 2 + 3 = 6.
<jupyter_code>
def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum = sum + i
    if(sum == n):
        return True
    else:
        return False

# Test the function
print(perfect_number(6))  # True
print(perfect_number(28))  # True
print(perfect_number(5))  # False
<jupyter_output>
True
True
False
<jupyter_text>
Question 3:Write a Python function to check if a given number is a prime number or not. A prime number is a number that has only two distinct positive divisors: 1 and itself. For example, the first six prime numbers are 2, 3, 5, 7, 11, and 13.
<jupyter_code>
def prime_number(n):
    if n <= 1: