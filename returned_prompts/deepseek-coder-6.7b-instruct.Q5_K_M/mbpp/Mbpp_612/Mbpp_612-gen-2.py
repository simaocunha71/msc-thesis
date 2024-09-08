
def merge(lst):
    return [[sub[i] for sub in lst] for i in range(2)]

print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']]))

