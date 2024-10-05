
def double_the_difference(lst):
    sum = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum += num ** 2
    return sum

print(double_the_difference([1, 3, 2, 0])) # 10
print(double_the_difference([-1, -2, 0])) # 0
print(double_the_difference([9, -2])) # 81
print(double_the_difference([0])) # 0
print(double_the_difference([])) # 0


def double_the_difference(lst):
    return sum(x ** 2 for x in lst if isinstance(x, int) and x > 0 and x % 2 != 0)

print(double_the_difference([1, 3, 2, 0])) # 10
print(double_the_difference([-1, -2, 0])) # 0
print(double_the_difference([9, -2])) # 81
print(double_the_difference([0])) # 0
print(double_the_difference([])) # 0


def double_the_difference(lst):
    return sum(filter(lambda x: isinstance(x, int) and x > 0 and x % 2 != 0, map(lambda x: x ** 2, lst)))

print(double_the_difference([1, 3, 2, 0])) # 10
print(double_the_difference([-1, -2, 0])) # 0
print(double_the_difference([9, -2])) # 81
print(double_the_difference([0])) # 0
print(double_the_difference([])) # 0


def double_the_difference(lst):
    return sum([x ** 2 for x in lst if type(x) == int and x > 0 and x % 2 != 0])

print(double_the