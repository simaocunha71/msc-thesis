def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_digits(345))

# Alternate solution
def sum_digits(n):
    return sum(map(int, str(n)))

print(sum_digits(345))
<jupyter_output>
12
12
<jupyter_text>
Question 2
<jupyter_code>
