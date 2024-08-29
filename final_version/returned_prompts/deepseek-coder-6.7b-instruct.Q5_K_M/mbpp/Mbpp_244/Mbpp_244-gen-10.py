def next_Perfect_Square(n):
    i = n+1
    while True:
        if int(i**0.5)**2 == i:
            return i
        i += 1

print(next_Perfect_Square(35))

# Output: 36

# Explanation: The next perfect square after 35 is 36.
<jupyter_output>
36
<jupyter_text>
**Problem 2**
<jupyter_code>
