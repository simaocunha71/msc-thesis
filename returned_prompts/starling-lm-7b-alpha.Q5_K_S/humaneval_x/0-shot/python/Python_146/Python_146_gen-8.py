
def specialFilter(nums):
    count = 0
    for i in nums:
        if len(str(i)) > 1:
            if int(str(i)[0]) % 2 != 0 and int(str(i)[-1]) % 2 != 0:
                count += 1
    return count

#tests
print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([33, -2, -3, 45, 21, 109, 44])) # 3




#alternative solution
def specialFilter(nums):
    count = 0
    for i in nums:
        if len(str(i)) > 1 and int(str(i)[0]) % 2 != 0 and int(str(i)[-1]) % 2 != 0:
            count += 1
    return count

#tests
print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([33, -2, -3, 45, 21, 109, 44])) # 3





#alternative solution
def specialFilter(nums):
    count = 0
    for i in nums:
        if len(str(i)) > 1 and (int(str(i)[0]) % 2 != 0 or int(str(i)[-1]) % 2 != 0):
            count += 1
    return count

#tests
print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([33, -2, -