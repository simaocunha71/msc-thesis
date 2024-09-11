def digit_distance_nums(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    diff = 0
    while num2 > 0:
        diff += abs(num1 % 10 - num2 % 10)
        num1 //= 10
        num2 //= 10
    return diff

# Test
print(digit_distance_nums(1, 2) == 1)

# Other solution
def digit_distance_nums(n1, n2):
    return sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str(n1)[::-1], str(n2)[::-1]))

print(digit_distance_nums(1, 2) == 1)

# Other solution
def digit_distance_nums(num1, num2):
    num1 = str(num1)[::-1]
    num2 = str(num2)[::-1]
    return sum(abs(int(num1[i])-int(num2[i])) for i in range(len(num1)))

print(digit_distance_nums(1, 2) == 1)

# Other solution
def digit_distance_nums(num1, num2):
    diff = 0
    while num2 > 0:
        diff += abs(num1 % 10 - num2 % 10)
        num1 //= 10
        num2 //= 10
    return diff

# Test
print(digit_distance_nums(1, 2) == 1)

# Other solution
def digit_distance_nums(n1, n2):
    return sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str(n1)[::-1], str(n2)[::-1]))

# Test
print(digit_distance_nums(1, 2) == 1)

# Other solution
def digit_distance_nums(num1, num