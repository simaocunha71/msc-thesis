def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(num)
            if int(str_num[0]) % 2 == 1 and int(str_num[-1]) % 2 == 1:
                count += 1
    return count

# Test cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2