def search(lst):
    from collections import Counter
    count = Counter(lst)
    for num, freq in count.items():
        if freq >= num:
            return num
    return -1

print(search([4, 1, 2, 2, 3, 1])) # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # 3
print(search([5, 5, 4, 4, 4])) # -1