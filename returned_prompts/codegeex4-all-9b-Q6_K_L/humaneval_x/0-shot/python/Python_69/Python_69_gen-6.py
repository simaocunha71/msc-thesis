def search(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    for item in sorted(count, reverse=True):
        if count[item] >= item:
            return item
    return -1

print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1