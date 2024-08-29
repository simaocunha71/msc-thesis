def double_the_difference(lst):
    sum = 0
    for i in lst:
        if i > 0 and i == int(i) and i % 2 != 0:
            sum += i**2
    return sum

C:
def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x == int(x) and x % 2 != 0)
