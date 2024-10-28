def specialFilter(nums):
    count = 0
    for num in nums:
        if abs(num) > 10 and num % 10 % 2 != 0 and abs(num) % 10 % 2 != 0:
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
print(specialFilter([12, 34, 56, 78]))  # Output: 0
print(specialFilter([11, 13, 15, 17]))  # Output: 4
print(specialFilter([-11, -13, -15, -17]))  # Output: 4
print(specialFilter([101, 103, 105, 107, 109]))  # Output: 5
print(specialFilter([-101, -103, -105, -107, -109]))  # Output: 5
print(specialFilter([100, 200, 300, 400, 500]))  # Output: 0
print(specialFilter([-100, -200, -300, -400, -500]))  # Output: 0
print(specialFilter([-99, -98, -97, -96, -95]))  # Output: 0
print(specialFilter([99, 98, 97, 96, 95]))  # Output: 0
print(specialFilter([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))  # Output: 0
print(specialFilter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # Output: 0
print(specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]))  # Output: 4
print(specialFilter([-11, -22, -33, -44, -55, -66, -77, -88, -99]))  # Output: 4
print(specialFilter([111, 222, 333, 444, 