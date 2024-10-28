    return sorted([i for i in x if len(set(map(int, str(i)))) == len(set(map(int, str(i)))) & all(not i % 2 for i in set(map(int, str(i))))])


