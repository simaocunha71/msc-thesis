
def double_the_difference(lst):
    sum_ = 0
    for i in lst:
        if i % 2 != 0 and i > 0:
            sum_ += i**2
    return sum_

# print(double_the_difference([1, 3, 2, 0]))  # 10
# print(double_the_difference([-1, -2, 0]))  # 0
# print(double_the_difference([9, -2]))  # 81
# print(double_the_difference([0]))  # 0


def double_the_difference(lst):
    sum_ = 0
    for i in lst:
        if i % 2 != 0 and i > 0:
            sum_ += i**2
    return sum_ if lst else 0

# print(double_the_difference([]))  # 0


def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and i > 0) if lst else 0

# print(double_the_difference([]))  # 0


def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and i > 0) if lst else 0

# print(double_the_difference([]))  # 0


def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and i > 0) if lst else 0

# print(double_the_difference([]))  # 0


def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and i > 0) if lst else 0

# print(double_the_difference([]))  # 0


def double_the_difference(lst):
    return sum(i**2 for i in lst if i % 2 != 0 and