def extract_index_list(l1,l2,l3):
    ans = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            ans.append(l1[i])
    return ans

#tests
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
print("tests pass")









"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.

Ex)

assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]


"""

def extract_index_list(l1,l2,l3):
    ans = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            ans.append(l1[i])
    return ans

#tests
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
print("tests pass")


```