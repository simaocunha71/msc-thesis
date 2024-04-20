"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""
def merge_sorted_list(l1, l2, l3):
    """write code here"""
    if len(set(l1)) + len(set(l2)) > 10:
        return []
    # [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    merged_list = []
    for i in range(len(l1)):
        if i < len(set(l1)) - len(set(l2)) + set(l1).index(l1[i]) - set(l2).index(l2[i]):
            merged_list.append(l1[i])
    else:
        for j in range(len(set(l2)) - len(set(l1)) + 1, len(l3)):
            if i < len(set(l3)) - set(l3).index(l3[j]):
                merged_list.append(l3[j])
    return merged_list
