def max_val(lst):
    num_list = [i for i in lst if isinstance(i, int)]
    return max(num_list)

print(max_val(['Python', 3, 2, 4, 5, 'version']))

"""
This function works similarly to the previous one, but