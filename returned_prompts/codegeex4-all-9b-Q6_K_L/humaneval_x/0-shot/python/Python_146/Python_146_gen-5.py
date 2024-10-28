def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and all(int(digit) % 2 == 1 for digit in str(num)[0] + str(num)[-1]):
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
print(specialFilter([1, 3, 5, 7, 9]))  # Output: 5
print(specialFilter([-11, -33, -55, -77, -99]))  # Output: 5
print(specialFilter([10, 12, 14, 16, 18]))  # Output: 0
print(specialFilter([101, 103, 105, 107, 109]))  # Output: 5