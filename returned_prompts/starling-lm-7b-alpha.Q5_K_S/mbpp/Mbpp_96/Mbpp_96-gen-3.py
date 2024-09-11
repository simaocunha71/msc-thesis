"""
def divisor(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count += 1
    return count

def divisor(n):
    return len([i for i in range(1,n+1) if n%i==0])

def divisor(n):
    return len([i for i in range(1,n+1) if n%i==0])
"""


def divisor(n):
    i = 1
    while i * i <= n:
        if (n % i == 0):
            if (n / i == i):
                return 1 + 1
            else:
                return 2 + 1
        i += 1
    return 1

# Test Cases:
print(divisor(1))  # 1
print(divisor(2))  # 2
print(divisor(3))  # 2
print(divisor(4))  # 3
print(divisor(5))  # 2
print(divisor(6))  # 4
print(divisor(7))  # 2
print(divisor(8))  # 4
print(divisor(9))  # 3
print(divisor(10))  # 4
print(divisor(12))  # 6
print(divisor(13))  # 2
print(divisor(14))  # 4
print(divisor(15))  # 4
print(divisor(16))  # 5
print(divisor(17))  # 2
print(divisor(18))  # 6
print(divisor(19))  # 2
print(divisor(20))  # 6
print(divisor(21))  # 4
print(divisor(22))  # 6
print(divisor(23))  # 2
print(divisor(24))  # 8
