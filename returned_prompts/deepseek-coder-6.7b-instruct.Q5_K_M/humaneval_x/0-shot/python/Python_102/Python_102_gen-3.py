
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    return -1

print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(20, 30))
print(choose_num(100, 100))
print(choose_num(111, 123))
print(choose_num(7, 9))
<jupyter_output>
14
-1
20
100
122
-1
<jupyter_text>
Problem 3: Write a Python function which takes an integer as input and returns a dictionary containing the count of each digit in the integer.
<jupyter_code>
