def merge(lst):
    return [[i[j] for i in lst] for j in range(2)]

print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']]))


