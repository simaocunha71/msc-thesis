
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    return -1

# test cases
print(choose_num(12, 15))  # 14
print(choose_num(13, 12))  # -1

# This function works by iterating from y down to x (inclusive) and checking 
# if each number is even. If it is, the function returns that number. If no 
# even number is found in that range, the function returns -1.
<jupyter_output>
14
-1
<jupyter_text>
Question 2: Write a Python function to convert the given integer to its binary representation.
<jupyter_code>
