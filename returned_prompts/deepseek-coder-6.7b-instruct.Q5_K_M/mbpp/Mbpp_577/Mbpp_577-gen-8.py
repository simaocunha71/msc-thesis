def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            while result % 10 == 0:
                result /= 10
            result = int(result % 100000)
        return result % 10

assert last_Digit_Factorial(4) == 4
"""
Idea: 
We calculate the factorial using a for loop and multiply the running result by the current number. We also continuously divide the result by 10 until the result is not divisible by 10, which effectively removes the trailing zeroes. We then convert the result to an integer and take the modulus of 100000 to ensure that the result fits within a 5-digit number. Finally, we return the last digit of the result by taking the modulus of 10.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2
<jupyter_code>
