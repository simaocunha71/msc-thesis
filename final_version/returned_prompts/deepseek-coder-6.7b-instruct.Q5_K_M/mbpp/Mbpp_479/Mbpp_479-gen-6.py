
def first_Digit(num):
    while num > 0:
        digit = num % 10
        if num == num:
            return digit
        num = num // 10
    return -1

assert first_Digit(123) == 1
assert first_Digit(456) == 4
assert first_Digit(789) == 7
assert first_Digit(0) == -1
<jupyter_output>
<empty_output>
<jupyter_text>
10. Write a Python function to find the last digit of a given number.
<jupyter_code>
