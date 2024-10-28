
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1

#Test cases
print(choose_num(12, 15)) #Should return 14
print(choose_num(13, 12)) #Should return -1
print(choose_num(21, 25)) #Should return 24
print(choose_num(16, 16)) #Should return 16
print(choose_num(10, 20)) #Should return 20
print(choose_num(100, 200)) #Should return 200
print(choose_num(1000, 2000)) #Should return 2000
print(choose_num(500, 1000)) #Should return 1000
print(choose_num(5000, 10000)) #Should return 10000
print(choose_num(1, 10000)) #Should return 10000
<jupyter_output>
14
-1
24
16
20
200
2000
1000
10000
10000
<jupyter_text>
Q2: Write a Python function to solve the quadratic equation. The function should take 3 arguments: `a`, `b`, and `c` which represent the coefficients of the quadratic equation `ax^2 + bx + c = 0`. The function should return the solution to the equation.
<jupyter_code>
