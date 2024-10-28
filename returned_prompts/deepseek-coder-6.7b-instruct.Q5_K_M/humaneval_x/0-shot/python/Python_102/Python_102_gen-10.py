
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1

# Test cases
print(choose_num(12, 15)) # 14
print(choose_num(13, 12)) # -1
print(choose_num(14, 15)) # 14
print(choose_num(15, 16)) # 16
print(choose_num(16, 17)) # 16
print(choose_num(17, 18)) # 18
print(choose_num(18, 19)) # 18
print(choose_num(19, 20)) # 20
<jupyter_output>
14
-1
14
16
16
18
18
20
<jupyter_text>
**Problem 10:**Write a Python function that takes in a string and returns the frequency of each character in the string.
<jupyter_code>
