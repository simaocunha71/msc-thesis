
def extract_index_list(l1, l2, l3):
    common = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common.append(l1[i])
    return common

print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

"""
This function works by iterating through each index of the lists. If the element at the current index in all three lists is the same, it is added to the "common" list. Once all indices have been checked, the "common" list is returned.
"""
<jupyter_output>
[1, 7]
<jupyter_text>
Question 2: Write a python function which accepts a list of numbers and returns the sum of all the elements in the list.
<jupyter_code>
