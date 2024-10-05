
    odd_product = 1

    for digit in str(n):
        if int(digit) % 2 != 0:
            odd_product *= int(digit)

    return odd_product if odd_product != 1 else 0

# Test cases
print(digits(1))  # Should return 1
print(digits(4))  # Should return 0
print(digits(235))  # Should return 15
print(digits(7159))  # Should return 95
print(digits(97531))  # Should return 7531
print(digits(58793))  # Should return 58793
print(digits(777777))  # Should return 7
print(digits(1234567890))  # Should return 3
<jupyter_output>
1
0
15
95
7531
58793
7
3
<jupyter_text>
Problem 2: Prime NumberCheck if a given number is a prime number.
<jupyter_code>
