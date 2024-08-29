
def min_k(records, k):
    return sorted(records, key=lambda x: x[1])[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

# Output: [('Akash', 2), ('Akshat', 4)]

"""
This function sorts the records by their second elements (which are the numbers) and takes the first k elements.
"""


