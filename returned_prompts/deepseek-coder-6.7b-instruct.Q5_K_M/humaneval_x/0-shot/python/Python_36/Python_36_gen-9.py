

def fizz_buzz(n: int):
    count = 0
    for i in range(1, n):
        if (i % 11 == 0 or i % 13 == 0):
            count += str(i).count('7')
    return count


print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3


# -----------------------------------
# Alternative solution with list comprehension:

def fizz_buzz(n: int):
    return sum(str(i).count('7') for i in range(1, n) if i % 11 == 0 or i % 13 == 0)


print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3

# -----------------------------------
# Alternative solution using while loop:

def fizz_buzz(n: int):
    count = 0
    i = 1
    while i < n:
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
        i += 1
    return count


print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3

# -----------------------------------
# Alternative solution using while loop and one liner:

def fizz_buzz(n: int):
    i, count = 1, 0
    while i < n:
        count += str(i).count('7') if i % 11 == 0 or i % 13 == 0 else 0
        i += 1
    return count


print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3

# 