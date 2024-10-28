
    return sum([int(abs(i) ** 2) for i in lst])

print(sum_squares([1, 4, 9]))
print(sum_squares([1.4, 4.2, 0]))
print(sum_squares([-2.4, 1, 1]))
print(sum_squares([1, 2, 3]))
print(sum_squares([1, 3, 5, 7]))





def sum_squares(lst):
    return sum([int(abs(i) ** 2) for i in lst])

print(sum_squares([1, 4, 9])) # 98
print(sum_squares([1.4, 4.2, 0])) # 29
print(sum_squares([-2.4, 1, 1])) # 6
print(sum_squares([1, 2, 3])) # 14
print(sum_squares([1, 3, 5, 7])) # 84
<jupyter_output>
98
29
6
14
84
<jupyter_text>
