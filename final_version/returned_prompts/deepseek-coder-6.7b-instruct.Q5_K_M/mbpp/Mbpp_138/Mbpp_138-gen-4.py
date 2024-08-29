def is_Sum_Of_Powers_Of_Two(n):
    i = 0
    while 2 ** i <= n:
        j = 0
        while 2 ** i + 2 ** j == n:
            return True
        j += 1
    i += 1
    return False

# Test Cases
print(is_Sum_Of_Powers_Of_Two(10))  # True
print(is_Sum_Of_Powers_Of_Two(14))  # True
print(is_Sum_Of_Powers_Of_Two(27))  # True
print(is_Sum_Of_Powers_Of_Two(33))  # False

# Test Case for 2^n
for i in range(32):
    print(is_Sum_Of_Powers_Of_Two(2 ** i))  # True

# Test Case for numbers that can't be represented as sum of non-zero powers of 2
for i in range(1, 100):
    if i not in [1, 2, 4, 8, 16, 32, 64]:
        print(is_Sum_Of_Powers_Of_Two(i))  # False

# Test Case for large number
print(is_Sum_Of_Powers_Of_Two(2 ** 32))  # True

# Test Case for negative number
print(is_Sum_Of_Powers_Of_Two(-1))  # False

# Test Case for zero
print(is_Sum_Of_Powers_Of_Two(0))  # False

# Test Case for 2^n + 2^m
for i in range(32):
    for j in range(32):
        print(is_Sum_Of_Powers_Of_Two(2 ** i + 2 ** j))  # True

# Test Case for numbers that can't be represented as sum of non-zero powers of 2
for i in range(-100, 0):
    print(is_Sum_Of_Powers_Of_Two(i)) 