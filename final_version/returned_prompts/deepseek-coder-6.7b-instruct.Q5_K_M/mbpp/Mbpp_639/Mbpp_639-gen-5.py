def sum_len_name(lst):
    return sum(len(name) for name in lst if not name[0].islower())

print(sum_len_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

This function uses a generator expression to iterate over the names in the list. It only includes the name in the sum if the first character of the name is not lowercase (checked by the `islower()` method). The `len()` function is used to calculate the length of each name. The results are then summed up by the `sum()` function.

This code will output `16` which is the sum of length of the names `'Dylan'`, `'Diana'`, `'Joanne'` and `'keith'` after removing the names that start with a lowercase letter.
<jupyter_output>
<empty_output>
<jupyter_text>
