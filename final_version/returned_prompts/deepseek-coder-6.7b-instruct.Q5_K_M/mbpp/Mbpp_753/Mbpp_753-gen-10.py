
def min_k(arr, k):
    return sorted(arr, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

# Output: [('Akash', 2), ('Akshat', 4)]

"""
In this function, we are using Python's built-in sorted() function, which sorts the array in increasing order by default. 
We also provide a custom key to the sorted() function, which is a lambda function that returns the second element of each tuple. 
This means that our array will be sorted by the second element of each tuple, in ascending order. 
Finally, we return the first k elements of the sorted array, which are the k tuples with the smallest second element.
"""

# If you need to find the maximum k records from the list, you can modify the key in lambda function to x[1] and use [::-1] to reverse the sorted list.
# For example:

def max_k(arr, k):
    return sorted(arr, key = lambda x: x[1])[::-1][:k]

print(max_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))

# Output: [('Manjeet', 10), ('Nikhil', 8)]
<jupyter_output>
[('Akash', 2), ('Akshat', 4)]
[('Manjeet', 10), ('Nikhil', 8)]
<jupyter_text>
