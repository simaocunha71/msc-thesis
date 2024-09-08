def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return n == sum

print(armstrong_number(153))
<jupyter_output>
True
<jupyter_text>
Q2:Write a function to find the factorial of a number.
<jupyter_code>
