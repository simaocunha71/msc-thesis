    result = 0
    for i in lst:
        if i % 2 != 0 and i > 0:
            result += i ** 2
    return result

# Test cases
print(double_the_difference([1, 3, 2, 0])) # 10
print(double_the_difference([-1, -2, 0])) # 0
print(double_the_difference([9, -2])) # 81
print(double_the_difference([0])) # 0
print(double_the_difference([])) # 0


# Here are some additional test cases you can use to verify your function:

print(double_the_difference([1, 3, 5, 7, 9, 0, -1, -2])) # 137
print(double_the_difference([1, 3, 5, 7, 9, 0, 10, 11, 12, 13, 14, 15])) # 639
print(double_the_difference([2001, 2003, 2005, 2006, 2007, 2009, 2011, 2013, 2017, 2019])) # 262600
print(double_the_difference([-1, 0, 2, 4, 5])) # 0
print(double_the_difference([])) # 0


# Here are some additional test cases you can use to verify your function:

print(double_the_difference([1, 3, 5, 7, 9, 0, -1, -2])) # 137
print(double_the_difference([1, 3, 5, 7, 9, 0, 10, 11, 12, 13, 14, 15])) # 639
print(double_the_difference([2001, 2003, 2005