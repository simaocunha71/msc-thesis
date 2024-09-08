
def add_dict_to_tuple(tpl, dic):
    tpl += (dic, )
    return tpl

print(add_dict_to_tuple((4, 5, 6), {"MSAM"  : 1, "is"  : 2, "best"  : 3} ))

"""
Output:
(4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""

