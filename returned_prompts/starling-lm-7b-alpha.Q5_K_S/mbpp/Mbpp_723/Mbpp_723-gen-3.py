def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

# assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4

# print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))




"""
The input is a string, and it is defined as a matrix of size n * m. The goal is to count the number of rows that are in ascending order.
assert count_asc_row(["ABC","CBA","BAC"])==2
"""

B:
def count_asc_row(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] > matrix[i][j+1]:
                break
        else:
            count += 1
    return count

# assert count_asc_row(["ABC","CBA","BAC"])==2

# print(count_asc_row(["ABC","CBA","BAC"]))




"""
The input is a list of strings, and each string is a combination of lowercase letters and digits. The goal is to count the number of strings that are not permutations of each other.
assert count_not_permutation(["123", "312"])==1
"""

C:
def count_not_permutation(list_str):
    count = 0
    for i in range(len(list_str)):
        for j in range(i+1, len(list_str)):
            if len(list_str[i]) == len(list_str[j]):
              