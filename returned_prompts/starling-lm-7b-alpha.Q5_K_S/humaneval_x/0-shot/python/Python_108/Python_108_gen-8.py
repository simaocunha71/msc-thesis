
def count_nums(arr):
    return sum(1 for num in arr if sum(map(int, str(abs(num)))) > 0)

# Alternative solution using reduce
from functools import reduce
def count_nums(arr):
    return sum(1 for num in arr if reduce(lambda acc, x: acc + int(x), str(abs(num))) > 0)


# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
print(count_nums([-10, -2, -3, 2, 3, 10, 12, 1]) == 5)
print(count_nums([1, 2, 3, 4, 5]) == 5)
print(count_nums([-100, -101, -102, 103, 104, 105]) == 3)
print(count_nums([-1000, -1001, -1002, 1003, 1004, 1005]) == 3)
print(count_nums([-10000, -10001, -10002, 10003, 10004, 10005]) == 3)


# Tests with negative numbers
print(count_nums([-1, 1, 1, 2]) == 4)
print(count_nums([-1, 11, -11, 11]) == 4)
print(count_nums([-1, 1, 1, -2]) == 3)
print(count_nums([-1, 1, 1, -3]) == 3)
print(count_nums([-1, 1, 1, -12]) == 3)
print(count_nums([-1, 1, 1