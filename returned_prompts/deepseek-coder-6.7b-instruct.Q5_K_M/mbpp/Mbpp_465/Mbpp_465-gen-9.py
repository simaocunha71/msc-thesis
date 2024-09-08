def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
This function takes a dictionary as input and returns a new dictionary with the same key-value pairs as the input dictionary, but without any key-value pairs where the value is None. This is done using a dictionary comprehension, which creates a new dictionary by iterating over the key-value pairs in the input dictionary and including only those where the value is not None.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4:Write a Python program to get the maximum and minimum value of a dictionary.
<jupyter_code>
def get_max_min(d):
    max_key = max(d, key=d.get)
    min_key = min(d, key=d.get)
    return max_key, d[max_key], min_key, d[min_key]

d = {'a': 5, 'b': 7, 'c': 1, 'd': 9}
max_key, max_value, min_key, min_value = get_max_min(d)
print(f'Max key: {max_key}, Max value: {max_value}')
print(f'Min key: {min_key}, Min value: {min_value}')
<jupyter_output>
Max key: d, Max value: 9
Min key: c, Min value: 1
<jupyter_text>
Question 5:Write a Python program to remove duplicates from Dictionary.
<jupyter_code>
def remove_duplicates(d):
    new_d = {}
    for key, value in d.items():
        if value not in new_d.values():
            new_d[key] = value
    return new_d

d = {'a': 1, 'b': 2, 'c': 1, 'd':