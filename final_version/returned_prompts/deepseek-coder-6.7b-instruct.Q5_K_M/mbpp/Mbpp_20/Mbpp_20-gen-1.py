"""
def is_woodall(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if sum(factors) % 2 == 0:
        return True
    else:
        return False

print(is_woodall(383))
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
