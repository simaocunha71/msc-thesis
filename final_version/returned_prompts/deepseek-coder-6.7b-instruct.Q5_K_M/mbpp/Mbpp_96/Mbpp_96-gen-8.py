def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))
<jupyter_output>
4
<jupyter_text>
Exercise 2: Write a Python function to find the sum of all divisors of a given integer.
<jupyter_code>
