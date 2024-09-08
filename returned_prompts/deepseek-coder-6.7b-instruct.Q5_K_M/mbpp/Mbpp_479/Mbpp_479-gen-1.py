
def first_Digit(n):
    while n >= 10:
        n /= 10
    return int(n)

print(first_Digit(123))

#output: 1
<jupyter_output>
1
<jupyter_text>
