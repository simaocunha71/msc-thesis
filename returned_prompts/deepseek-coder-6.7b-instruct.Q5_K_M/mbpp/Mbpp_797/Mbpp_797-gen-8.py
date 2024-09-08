def sum_in_range(l, r):
    sum = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_in_range(2,5))

# Alternative solution:
def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)

print(sum_in_range(2,5))

# Alternative solution:
def sum_in_range(l, r):
    return sum(i for i in range(l+1 if l%2 else l, r+1, 2))

print(sum_in_range(2,5))
<jupyter_output>
8
8
8
<jupyter_text>
Question 14
<jupyter_code>
