
def even_odd_count(num):
    even = 0
    odd = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

print(even_odd_count(-12))
print(even_odd_count(123))
<jupyter_output>
(1, 1)
(1, 2)
<jupyter_text>
Problem 8:
<jupyter_code>
