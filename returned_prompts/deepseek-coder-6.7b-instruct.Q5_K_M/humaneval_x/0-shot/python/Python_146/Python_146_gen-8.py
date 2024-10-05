
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and str(num)[0] in '13579' and str(num)[-1] in '13579':
            count += 1
    return count

print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99])) # 6
print(specialFilter([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # 0
print(specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # 0
print(specialFilter([101, 222, 333, 444, 555, 666, 777, 888, 999, 1000])) # 10
print(specialFilter([-101, -222, -333, -444, -555, -666, -777, -888, -999, -1000])) # 0
print(specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])) # 10
print(specialFilter([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])) # 0
print(specialFilter([101, 112, 133, 144, 155, 166, 177, 188, 1