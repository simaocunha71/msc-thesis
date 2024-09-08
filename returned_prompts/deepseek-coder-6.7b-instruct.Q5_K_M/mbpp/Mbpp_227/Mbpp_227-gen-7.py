def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

print(min_of_three(10,20,0)) # Output: 0

# Task 3
