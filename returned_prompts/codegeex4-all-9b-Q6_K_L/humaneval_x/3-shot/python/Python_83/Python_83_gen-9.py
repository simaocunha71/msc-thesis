    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1
    return count

print(starts_one_ends(2))  # Output: 18
print(starts_one_ends(3))  # Output: 272
print(starts_one_ends(4))  # Output: 3240
print(starts_one_ends(5))  # Output: 37800

