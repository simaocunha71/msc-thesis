
def extract_index_list(l1,l2,l3):
    common_elements = []
    for i in range(len(l1)):
        if l1[i]==l2[i]==l3[i]:
            common_elements.append(l1[i])
    return common_elements

print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

"""
This function works by iterating through each index of the first list and checking if the same index in the second and third lists also has the same value. If it does, it adds that value to the 'common_elements' list. The function returns this list.
"""
<jupyter_output>
[1, 7]
<jupyter_text>
Question 2
<jupyter_code>
