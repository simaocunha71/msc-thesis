def find_tuples(list_of_tuples, k):
    result = []
    for t in list_of_tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result
list_of_tuples = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
k = 6