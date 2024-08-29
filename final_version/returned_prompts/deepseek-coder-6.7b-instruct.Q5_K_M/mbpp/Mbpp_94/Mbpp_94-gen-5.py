def index_minimum(lst):
    lst.sort(key = lambda x: x[1])
    return lst[0][0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

