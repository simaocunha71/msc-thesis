"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

def Find_Max(L):
    max_len = L[0].copy()
    for i in range(1,len(L)):
        if L[i] is not None:
            print('Checking the length of '+str(L[i]))
            if (max_len == []) or len(max_len) < len(L[i]): # Checks if max_len is empty and if the current element in L is bigger than max_len
                max_len = L[i].copy()
        else:
            print('Null element found')
    return max_len

# Driver code
print("Maximum length of a list containing elements with null value is : ",Find_Max([['A'],['A','B'],['A','B','C']]))