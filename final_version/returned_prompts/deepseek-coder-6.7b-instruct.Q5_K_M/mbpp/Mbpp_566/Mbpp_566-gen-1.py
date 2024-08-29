
def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

print(sum_digits(345))
<jupyter_output>
12
<jupyter_text>
Question 5
<jupyter_code>
