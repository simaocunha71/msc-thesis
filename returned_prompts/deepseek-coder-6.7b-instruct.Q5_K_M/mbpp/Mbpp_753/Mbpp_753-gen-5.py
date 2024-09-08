def min_k(records, k):
    # sort by second element of tuple
    records.sort(key = lambda x: x[1])
    return records[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

# Output: [('Akash', 2),  ('Akshat', 4)]

"""
Explanation:
This function works by first sorting the input list of tuples by the second element of each tuple (which is what we want to minimize). It then returns the first k tuples from this sorted list.
"""
<jupyter_output>
[('Akash', 2), ('Akshat', 4)]
<jupyter_text>
2. Write a Python function to find the maximum k records from tuple list.
<jupyter_code>
