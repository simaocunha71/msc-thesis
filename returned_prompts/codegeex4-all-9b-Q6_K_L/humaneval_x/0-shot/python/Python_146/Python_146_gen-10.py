def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and (num % 10) % 2 == 1 and (num // 10) % 2 == 1:
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2