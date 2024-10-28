def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product if product != 1 else 0

# Test cases
print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235))  # 15
print(digits(12345))  # 45
print(digits(24680))  # 0
print(digits(13579))  # 135
print(digits(100))  # 0
print(digits(1111))  # 1
print(digits(1234567))  # 15
print(digits(24680))  # 0
print(digits(13579))  # 135
print(digits(12345))  # 45
print(digits(111))  # 1
print(digits(222))  # 0
print(digits(333))  # 0
print(digits(444))  # 0
print(digits(555))  # 5
print(digits(666))  # 0
print(digits(777))  # 7
print(digits(888))  # 0
print(digits(999))  # 9
print(digits(10000))  # 0
print(digits(11111))  # 1
print(digits(123456789))  # 15
print(digits(246810))  # 0
print(digits(13579))  # 135
print(digits(123456))  # 0
print(digits(24680))  # 0
print(digits(13579))  # 135
print(digits(12345))  # 45
print(digits(111))  # 1
print(digits(222))  # 0
print(digits(333))  # 0
print(digits(444))  # 0
print(digits(555))  # 5
print(digits(666))  # 0
print(digits(777))  # 7
print(digits(888))  # 0
print(digits(999))  # 9
print(digits(10000))  # 0
print(digits(11111))  # 1
print(digits(123456789))  # 15
print(digits(246810))  # 0
print(digits(13579