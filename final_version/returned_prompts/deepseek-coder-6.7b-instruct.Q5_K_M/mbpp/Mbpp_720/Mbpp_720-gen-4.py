def add_dict_to_tuple(t, d):
    return t + (d,)

t = (4, 5, 6)
d = {"MSAM"  : 1, "is" : 2, "best"  : 3}
print(add_dict_to_tuple(t, d))

#output
#(4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})


