
def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements

print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

# Output: [1, 7]

"""
This function works by iterating through the elements of the input lists at the same index. If an element is the same in all three lists at the same index, that element is added to the 'common_elements' list. Finally, the function returns the 'common_elements' list.
"""

# End of solution

