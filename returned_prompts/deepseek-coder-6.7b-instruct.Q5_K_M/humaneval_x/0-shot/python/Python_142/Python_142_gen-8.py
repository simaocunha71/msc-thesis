


def sum_squares(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i]**2
        elif i % 4 == 0:
            sum += lst[i]**3
        else:
            sum += lst[i]
    return sum
<jupyter_output>
<empty_output>
<jupyter_text>
Test Cases:
<jupyter_code>
print(sum_squares([1,2,3])) # 6
print(sum_squares([])) # 0
print(sum_squares([-1,-5,2,-1,-5])) # -126
<jupyter_output>
6
0
-126
<jupyter_text>
