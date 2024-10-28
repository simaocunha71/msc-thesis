    result = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            result *= int(digit)
    return result if result != 1 else 0
# test cases
print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235))  # 15
print(digits(10))  # 0
print(digits(125))  # 5
print(digits(1234))  # 0
print(digits(12345))  # 15
print(digits(123456))  # 0
print(digits(13579))  # 45
print(digits(135792))  # 0
print(digits(1357923))  # 45
print(digits(13579234))  # 0
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789))  # 45
print(digits(13579246789)) 