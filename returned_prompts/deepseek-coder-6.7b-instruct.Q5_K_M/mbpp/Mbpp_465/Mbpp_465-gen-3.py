def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

# {'c1': 'Red', 'c2': 'Green'}

"""
This function works by using a dictionary comprehension to create a new dictionary that includes only the key-value pairs from the original dictionary where the value is not None.
"""
<jupyter_output>
{'c1': 'Red', 'c2': 'Green'}
<jupyter_text>
Question 2:
<jupyter_code>
