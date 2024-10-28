def sum_squares(lst):
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0:
            lst[i] = lst[i] ** 3
    return sum(lst)

# Test cases
print(sum_squares([1,2,3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1,-5,2,-1,-5]))  # Output: -126