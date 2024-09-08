def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

assert not is_perfect_square(10)
"""
The function works by using the Babylonian method to approximate square roots. It starts with an initial guess, and then improves the guess until it is accurate to within one digit. The function keeps track of the previously seen guesses to detect infinite loops.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2**
<jupyter_code>
