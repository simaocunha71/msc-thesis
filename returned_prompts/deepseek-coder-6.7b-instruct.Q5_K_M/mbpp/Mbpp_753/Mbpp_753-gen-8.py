
def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

assert min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2) == [('Akash', 2),  ('Akshat', 4)]
"""

