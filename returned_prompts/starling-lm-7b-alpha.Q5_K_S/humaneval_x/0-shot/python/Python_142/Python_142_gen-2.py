
def sum_squares(lst):
    total = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            lst[i] = lst[i] ** 3
    for i in lst:
        total += i
    return total

# print(sum_squares([1,2,3])) # 6
# print(sum_squares([])) # 0
# print(sum_squares([-1,-5,2,-1,-5])) # -126





```
