def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and int(str(num)[0]) % 2 == 1 and int(str(num)[-1]) % 2 == 1:
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # => 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # => 2