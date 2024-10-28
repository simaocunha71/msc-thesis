def check_type(tup):
    return all(isinstance(i, type(tup[0])) for i in tup)

print(check_type((5, 6, 7, 3, 5, 6) ))


