
def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

"""
The function `min_k` takes a list and an integer `k` as input and returns the `k` records with minimum values. The function uses the built-in `sorted` function to sort the list of tuples based on the second elements of the tuples. The `key` argument of the `sorted` function is set to a lambda function that returns the second element of each tuple (`x[1]`). The `:k` slice operation is used to get the first `k` elements of the sorted list.

The output of the function call `min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2)` will be `[('Akash', 2),  ('Akshat', 4)]`.
"""
<jupyter_output>
[('Akash', 2), ('Akshat', 4)]
<jupyter_text>
**Problem 3**
<jupyter_code>
