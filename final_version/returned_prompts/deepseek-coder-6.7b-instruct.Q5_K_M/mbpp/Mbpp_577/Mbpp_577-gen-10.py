def last_Digit_Factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial % 10

print(last_Digit_Factorial(4))

# Output: 4

# Explanation: The factorial of 4 is 24. The last digit of 24 is 4.
<jupyter_output>
4
<jupyter_text>
