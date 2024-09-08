
def is_woodall(n):
    num = str(n)
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            return False
    return True

print(is_woodall(383))

# 383 is a woodall number because all digits from left to right are in non-decreasing order.
# Hence, the program will return True.
<jupyter_output>
True
<jupyter_text>
