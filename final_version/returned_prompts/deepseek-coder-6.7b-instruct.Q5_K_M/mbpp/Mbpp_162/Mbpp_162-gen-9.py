def sum_series(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total

print(sum_series(6))

# Alternate solution using formula
def sum_series_alt(n):
    return n * (n // 2)

print(sum_series_alt(6))

# Both solutions will return 12.
<jupyter_output>
12
12
<jupyter_text>
Question 2
<jupyter_code>
