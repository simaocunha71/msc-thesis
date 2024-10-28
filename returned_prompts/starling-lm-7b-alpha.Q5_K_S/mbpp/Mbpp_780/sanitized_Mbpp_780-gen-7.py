def find_combinations(tuples):
    result = set()
    for t1 in tuples:
        for t2 in tuples:
            if t1[0] + t2[0] in result:
                continue
            result.add(t1[0] + t2[0])
    return result