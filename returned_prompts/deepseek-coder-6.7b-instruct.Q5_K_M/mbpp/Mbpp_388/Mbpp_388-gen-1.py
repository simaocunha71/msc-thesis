
def highest_Power_of_2(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return 2 ** (i - 1)

print(highest_Power_of_2(10))

# Alternate Solution using bitwise operators

def highest_Power_of_2(n):
    i = 0
    while (1 << i) <= n:
        i += 1
    return (1 << (i - 1))

print(highest_Power_of_2(10))
<jupyter_output>
8
8
<jupyter_text>
Question 2
<jupyter_code>
