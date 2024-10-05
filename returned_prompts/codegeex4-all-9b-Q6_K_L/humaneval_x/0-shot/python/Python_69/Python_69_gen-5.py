def search(lst):
    freqs = {}
    for el in lst:
        freqs[el] = freqs.get(el, 0) + 1
    for el in freqs:
        if freqs[el] >= el:
            return el
    return -1

print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))