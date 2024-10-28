def double_the_difference(lst):
    total = 0
    for i in lst:
        if i > 0 and i % 2 != 0:
            total += i ** 2
    return total * 2

print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))