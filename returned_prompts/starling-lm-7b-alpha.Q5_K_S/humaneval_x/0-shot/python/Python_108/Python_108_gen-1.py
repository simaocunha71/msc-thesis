
def count_nums(arr):
    count = 0
    for num in arr:
        if sum(map(int, str(abs(num)))) > 0:
            count += 1
    return count


# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
print(count_nums([100, 1000, -100, -1000]) == 2)
print(count_nums([-1000000000000000000, -100000000000000000, -10000000000000000, 10000000000000000, 1000000000000000000]) == 2)
print(count_nums([1000000000000000000, 100000000000000000, 10000000000000000, -10000000000000000, -100000000000000000]) == 3)


# count_nums([]) -> 0
# count_nums([-1, 11, -11]) -> 1
# count_nums([1, 1, 2]) -> 3
# count_nums([100, 1000, -100, -1000]) -> 2
# count_nums([-1000000000000000000, -100000000000000000, -1000000000000