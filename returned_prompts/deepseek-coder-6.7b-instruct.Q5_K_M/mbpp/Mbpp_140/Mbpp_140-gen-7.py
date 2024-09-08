"""
def extract_singly(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

print(set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])))
"""

R:
"""
{1, 3, 4, 5, 7}
"""


