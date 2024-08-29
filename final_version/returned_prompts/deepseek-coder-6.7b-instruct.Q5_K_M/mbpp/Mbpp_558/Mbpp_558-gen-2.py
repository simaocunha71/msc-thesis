def digit_distance_nums(num1, num2):
    return sum(abs(int(a)-int(b)) for a, b in zip(str(num1), str(num2)))

print(digit_distance_nums(123, 321))  # 4
print(digit_distance_nums(1, 2))  # 1
print(digit_distance_nums(12, 21))  # 2
print(digit_distance_nums(100, 200))  # 1

# 4. Write a Python function that calculates the sum of all prime numbers up to a given limit.

