def find_tuples(lst, k):
    result = []
    for t in lst:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))


