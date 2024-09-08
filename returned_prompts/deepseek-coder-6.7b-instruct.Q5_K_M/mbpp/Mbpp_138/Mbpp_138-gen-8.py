def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    if n == 1 or n == 2:
        return True
    while n > 1:
        power = 0
        while 2**power <= n:
            if 2**power == n:
                return True
            power += 1
        n -= 1
    return False

assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(12) == True
assert is_Sum_Of_Powers_Of_Two(23) == True
assert is_Sum_Of_Powers_Of_Two(33) == False
"""
This function works by decrementing the number `n` and checking if it equals the power of 2. If it does, it returns True. If it doesn't find a match, it decrements `n` again and checks again. This process repeats until `n` is 1. If it never finds a match, it returns False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
