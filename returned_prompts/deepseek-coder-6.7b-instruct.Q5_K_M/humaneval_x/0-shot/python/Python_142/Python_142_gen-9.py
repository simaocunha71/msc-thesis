


    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i] ** 2
        elif i % 4 == 0:
            sum += lst[i] ** 3
        else:
            sum += lst[i]
    return sum



# Test cases
print(sum_squares([1,2,3]))  # 6
print(sum_squares([]))  # 0
print(sum_squares([-1,-5,2,-1,-5]))  # -126
print(sum_squares([1,2,3,4,5,6,7,8,9,10]))  # 212
print(sum_squares([1,1,1,1,1,1,1,1,1,1]))  # 28
print(sum_squares([0,0,0,0,0,0,0,0,0,0]))  # 0
<jupyter_output>
6
0
-126
212
28
0
<jupyter_text>
