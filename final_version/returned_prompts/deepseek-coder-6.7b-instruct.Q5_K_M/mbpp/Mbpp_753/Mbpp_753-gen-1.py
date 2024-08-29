"""
def min_k(tuples, k):
    return sorted(tuples, key=lambda x: x[1])[:k]
"""

# Function to get the minimum k records from a list of tuples.
def min_k(tuples, k):
    return sorted(tuples, key=lambda x: x[1])[:k]

# Testing the function
print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

# Expected output: [('Akash', 2),  ('Akshat', 4)]

# Note: This function sorts the tuples in ascending order by their second element (i.e., the value) and returns the first k tuples.
<jupyter_output>
[('Akash', 2), ('Akshat', 4)]
<jupyter_text>
