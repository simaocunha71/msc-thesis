"""
def common_in_nested_lists(nested_lists):
    common = []
    for i in range(len(nested_lists[0])):
        for j in range(1, len(nested_lists)):
            if nested_lists[j][i] not in nested_lists[j-1]:
                break
        else:
            common.append(nested_lists[0][i])
    return common
"""

