def extract_index_list(l1,l2,l3):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            l.append(l1[i])
    return l

# assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]



"""
Given a string and an integer k, write a function that returns all the possible permutations of the string with a length equal to the integer k.

If there are duplicate characters in the string, it is still possible to form a permutation with duplicate characters.
"""

def permutation(string, k):
    result = []
    if k == 0:
        result.append("")
        return result
    else:
        temp = permutation(string, k-1)
        for i in range(len(string)):
            for j in range(len(temp)):
                result.append(temp[j]+string[i])
    return result

# print(permutation("abc", 2))

"""
Given a string, find the length of the longest substring that does not have the same character consecutively.
"""

def longest_substring(string):
    result = 0
    count = 1
    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            count = 1
        else:
            count += 1
        result = max(result,count)
    return result+1

# print(longest_substring("aaabbbccccddeeeee"))


"""
Given a string, find the length of the longest substring that contains no duplicate characters.
"""
def longest_substring_with_no_duplicate(string):
    result = 0
    count = 1
    for i in range(1,len