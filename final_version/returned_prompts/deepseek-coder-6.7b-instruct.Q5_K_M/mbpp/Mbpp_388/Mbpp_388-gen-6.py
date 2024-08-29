
def highest_Power_of_2(n):
    i = 0
    while True:
        val = 2 ** i
        if val > n:
            return 2 ** (i - 1)
        i += 1

print(highest_Power_of_2(10))
<jupyter_output>
8
<jupyter_text>
