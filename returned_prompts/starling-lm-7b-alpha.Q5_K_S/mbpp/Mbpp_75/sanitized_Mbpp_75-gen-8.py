def find_tuples(list_of_tuples, k):
    result = []
    for t in list_of_tuples:
        all_divisible = True
        for elem in t:
            if elem % k != 0:
                all_divisible = False
                break
        if all_divisible:
            result.append(t)
    return result