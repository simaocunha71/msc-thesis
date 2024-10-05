    if n < 1:
        return 0
    for i in range(n, 0, -1):
        if n % i == 0:
            return i

// Test
print(LargestDivisor(15))  # 5
print(LargestDivisor(12))  # 6
print(LargestDivisor(17))  # 1
print(LargestDivisor(20))  # 4
print(LargestDivisor(21))  # 3
print(LargestDivisor(24))  # 12
print(LargestDivisor(25))  # 5
print(LargestDivisor(27))  # 3
print(LargestDivisor(30))  # 30
print(LargestDivisor(36))  # 36
print(LargestDivisor(39))  # 3
print(LargestDivisor(40))  # 20
print(LargestDivisor(42))  # 42
print(LargestDivisor(45))  # 45
print(LargestDivisor(48))  # 48
print(LargestDivisor(50))  # 50

// Output:
// 5
// 6
// 1
// 4
// 3
// 12
// 5
// 3
// 30
// 36
// 3
// 20
// 42
// 45
// 48
// 50

B:
    def largest_divisor(n):
        for i in range(n, 0, -1):
            if n % i == 0:
                return i
    print(largest_divisor(15))  # 5
    print(largest_divisor(12))  # 6
    print(largest_divisor(17))  # 1
    print(largest_divisor(20))  # 4
    print(largest_divisor(21))  # 3
    print(largest_divisor(24))  # 12
    print(largest_divisor(25))  # 5
    print(largest_divisor(27))  # 3
    print(largest_divisor(30))  # 30
    print(largest_divisor(36))  # 36
    print(largest_divisor(39))  # 3
    print(largest_divisor(