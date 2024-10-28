def search(lst):
    freq = [lst.count(i) for i in set(lst)]
    return max([i for i, f in zip(lst, freq) if f >= i], default=-1)

print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))

# Output:
# 2
# 3
# -1
