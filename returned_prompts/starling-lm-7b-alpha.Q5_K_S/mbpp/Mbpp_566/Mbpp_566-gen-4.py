"""
def sum_digits(n):
    result = 0
    while n:
        result += n % 10
        n = n // 10
    return result
"""

def sum_digits(n):
    result = 0
    while n:
        result += n % 10
        n = n // 10
    return result

# 测试
assert sum_digits(345) == 12

# 测试更多
print(sum_digits(12345))
print(sum_digits(123456))
print(sum_digits(1234567))
print(sum_digits(12345678))
print(sum_digits(123456789))
print(sum_digits(1234567890))
print(sum_digits(12345678901))
print(sum_digits(123456789012))
print(sum_digits(1234567890123))
print(sum_digits(12345678901234))
print(sum_digits(123456789012345))
print(sum_digits(1234567890123456))
print(sum_digits(12345678901234567))
print(sum_digits(123456789012345678))
print(sum_digits(1234567890123456789))
print(sum_digits(12345678901234567890))
print(sum_digits(123456789012345678901))
print(sum_digits(1234567890123