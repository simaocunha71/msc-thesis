def is_Sum_Of_Powers_Of_Two(n):
    for i in range(n):
        if 2**i == n:
            return True
        if 2**i > n:
            break
    return False

print(is_Sum_Of_Powers_Of_Two(10))

"""
Here, we are checking each power of 2 from 0 to n. If any power of 2 equals to n, we return True. If we find any power of 2 greater than n, we break the loop and return False.
"""
<jupyter_output>
True
<jupyter_text>
Q10.
<jupyter_code>
