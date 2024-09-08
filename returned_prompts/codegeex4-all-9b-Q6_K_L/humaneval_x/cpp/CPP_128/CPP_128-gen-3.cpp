def prod_signs(arr):
    if not arr:
        return -32768
    sign = 1
    for i in arr:
        if i < 0:
            sign *= -1
        elif i == 0:
            return 0
    return sum(abs(i) for i in arr) * sign

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
print(prod_signs([-1, -2, -2, 4]))

def prod_signs(arr):
    if not arr:
        return -32768
    sign = 1
    for i in arr:
        if i < 0:
            sign *= -1
        elif i == 0:
            return 0
    return sum(abs(i) for i in arr) * sign

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
print(prod_signs([-1, -2, -2, 4]))


def prod_signs(arr):
    if not arr:
        return -32768
    sign = 1
    for i in arr:
        if i < 0:
            sign *= -1
        elif i == 0:
            return 0
    return sum(abs(i) for i in arr) * sign

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
print(prod_signs([-1, -2, -2, 4]))


def prod_signs(arr):
    if not arr:
        return -32768
    sign = 1
    for i in arr:
        if i < 0:
            sign *= -1
        elif i == 0:
            return 0
    return sum(abs(i) for i in arr) * sign

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
print(prod_signs([-1, -2, -2, 4]))

def prod_signs(arr):
    if not arr:
        return -32768
    sign = 1
    for i in arr:
        if i < 0:
            sign *= -1