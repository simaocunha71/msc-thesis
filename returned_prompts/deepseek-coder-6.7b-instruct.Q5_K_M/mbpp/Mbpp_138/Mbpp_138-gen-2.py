def is_Sum_Of_Powers_Of_Two(n):
    i = 0
    while 2 ** i <= n:
        j = 0
        while 2 ** i + 2 ** j == n:
            return True
        j += 1
    i += 1
    return False

print(is_Sum_Of_Powers_Of_Two(10))
<jupyter_output>
True
<jupyter_text>
Problem 2
<jupyter_code>
