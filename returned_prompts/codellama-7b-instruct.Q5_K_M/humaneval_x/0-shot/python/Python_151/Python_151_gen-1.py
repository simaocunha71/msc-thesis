
def double_the_difference(lst):
    # Write your code here
    if not lst:
        return 0
    odd = [num**2 for num in lst if num % 2 != 0 and num > 0]
    even = [num**2 for num in lst if num % 2 == 0 and num > 0]
    return sum(odd) - sum(even)


def double_the_difference(lst):
    if not lst:
        return 0
    return sum(x**2 for x in lst if x > 0 and x % 2) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2 != 0) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2 != 0) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2 != 0) - sum(x**2 for x in lst if x > 0 and x % 2 == 0)


def double_the_difference(lst):
    return sum(x**2 for x in lst if x > 0 and x % 2) - sum(