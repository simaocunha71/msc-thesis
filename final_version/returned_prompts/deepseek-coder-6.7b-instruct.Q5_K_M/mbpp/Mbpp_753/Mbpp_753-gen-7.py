
def min_k(records, k):
    return sorted(records, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil',_ 8)], 2))


