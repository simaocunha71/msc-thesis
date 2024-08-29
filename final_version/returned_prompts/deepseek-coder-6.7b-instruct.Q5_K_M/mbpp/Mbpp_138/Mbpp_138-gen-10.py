def is_Sum_Of_Powers_Of_Two(num):
    i = 0
    while 2 ** i <= num:
        if 2 ** i == num:
            return True
        i += 1
    return False

print(is_Sum_Of_Powers_Of_Two(10))  # True
<jupyter_output>
True
<jupyter_text>
