def difference(n):
    return (sum(i**3 for i in range(1, n+1)) - sum(i for i in range(1, n+1)))

print(difference(3))

# Output: 30

# Explanation:
# The sum of cubes of the first 3 natural numbers is 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
# The sum of the first 3 natural numbers is 1 + 2 + 3 = 6
# So, the difference is 36 - 6 = 30.


# To check:
assert difference(3) == 30
<jupyter_output>
30
<jupyter_text>
Question 2
<jupyter_code>
