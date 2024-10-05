def sum_squares(lst):
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0:
            lst[i] = lst[i] ** 3
    return sum(lst)

print(sum_squares([1,2,3])) # 6
print(sum_squares([])) # 0
print(sum_squares([-1,-5,2,-1,-5])) # -126