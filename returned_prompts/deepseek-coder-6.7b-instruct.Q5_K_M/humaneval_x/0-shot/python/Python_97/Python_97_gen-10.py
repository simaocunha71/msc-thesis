
def multiply(a, b):
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    return a_unit * b_unit

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20


# This solution works by taking the modulo 10 of the absolute values of the inputs,
# which gives the unit digit of each number. It then multiplies these unit digits
# together to give the required product. The use of abs ensures that the unit
# digit is always positive, even if the input was negative.
<jupyter_output>
16
72
0
20
<jupyter_text>
Solution 2:
<jupyter_code>
def multiply(a, b):
    return (a % 10) * (b % 10)
<jupyter_output>
<empty_output>
<jupyter_text>
Solution 3:
<jupyter_code>
def multiply(a, b):
    return (abs(a) % 10) * (abs(b) % 10)
<jupyter_output>
<empty_output>
<jupyter_text>
Solution 4:
<jupyter_code>
def multiply(a, b):
    a = str(a) if a >= 0 else str(a)[1]
    b = str(b) if b >= 0 else str(b)[1]
    return int(a)*int(b)
<jupyter_output>
<empty_output>
<jupyter_text>
Solution 5:
<jupyter_code>
def multiply(a, b):
    a = abs(a) if a >= 0 else -abs(a)
