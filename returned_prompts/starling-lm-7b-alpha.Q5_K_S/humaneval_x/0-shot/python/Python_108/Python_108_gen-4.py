
def count_nums(arr):
    return sum(1 for n in arr if sum(map(int, str(abs(n)))) > 0)

# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)





def count_nums(arr):
    return sum(1 for n in arr if sum(map(int, str(abs(n)))) > 0)

# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)





def count_nums(arr):
    count = 0
    for n in arr:
        if sum(map(int, str(abs(n)))) > 0:
            count += 1
    return count

# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)




def count_nums(arr):
    count = 0
    for n in arr:
        if sum(map(int, str(abs(n)))) > 0:
            count += 1
    return count

# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)




def count_nums(arr):
    return len([n for n in arr if sum(map(int, str(abs(n)))) > 0])

# Tests
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count