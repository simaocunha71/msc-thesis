def move_num(s):
    n_list = []
    for i in s:
        if i.isdigit():
            n_list.append(i)
    for i in n_list:
        s = s.replace(i, '')
    return s + "".join(n_list)

# def move_num(s):
#     n_list = []
#     for i in s:
#         if i.isdigit():
#             n_list.append(i)
#     for i in range(len(n_list)):
#         s = s.replace(n_list[i], '')
#     return s + "".join(n_list)

print(move_num('I1love143you55three3000thousand'))
# print(move_num("I1love143you55three3000thousand"))

"""
Runtime Error: maximum recursion depth exceeded while processing the function move_num

This error occurs because we use the replace method in python, and it's not thread-safe.
So, it's better to use the join method instead of the replace method in this case.
"""

# Python3 program to print all permutations of string

''' Helper function that swaps
    the characters at position
    i with the character at
    position j in the string '''
def swap(s, i, j):
    temp = list(s)
    temp[i], temp[j] = temp[j], temp[i]
    return ''.join(temp)

''' Function to print all permutations
    of string This function takes three
    parameters:
    1. String
    2. Starting index of the string
    3. Ending index of the string. '''
def permute(s, l, r):

    if l == r:
        print(s)
    else:
        for i in range(l, r + 1):
            s = swap(s, l, i)
            permute(s, l + 1, r)
            s = swap(s, l, i)

# Driver code
if __name__ ==