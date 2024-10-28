def search(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num in frequency:
        if frequency[num] >= num:
            return num

    return -1

print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1