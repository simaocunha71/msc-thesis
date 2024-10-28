


    sum_ = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum_ += lst[i] ** 2
        elif i % 4 == 0:
            sum_ += lst[i] ** 3
        else:
            sum_ += lst[i]
    return sum_


print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([1, 2, 3, 4, 5]))  # Output: 21
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 131
<jupyter_output>
6
0
-126
21
131
<jupyter_text>
Question 3:
<jupyter_code>
