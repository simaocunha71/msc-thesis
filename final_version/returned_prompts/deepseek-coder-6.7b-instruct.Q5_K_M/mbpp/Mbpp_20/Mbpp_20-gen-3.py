
def is_woodall(n):
    if n < 10:
        return False
    else:
        str_n = str(n)
        sum_of_digits = sum(int(digit) for digit in str_n)
        return n % sum_of_digits == 0

assert is_woodall(383) == True
assert is_woodall(12) == False
assert is_woodall(100) == True
assert is_woodall(21) == False
assert is_woodall(145) == False
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Sum of Numerical Digits of a NumberA numerical digit is a single digit (0-9). The sum of the numerical digits of a number is the sum of its digits.For example, the sum of the numerical digits of the number 1234 is 1+2+3+4 = 10.Given a number n, write a function that calculates the sum of the numerical digits of n.
<jupyter_code>
