def is_Sub_Array(arr1, arr2):
    if len(arr2) > len(arr1):
        return False
    for i in range(len(arr1)-len(arr2)+1):
        if arr2 == arr1[i:i+len(arr2)]:
            return True
    return False

# Python3 program to check if one list is sub-sequence
# of another list or not

# Returns true if b is a sub-sequence of a
def check_subsequence(a, b):
    m = len(a)
    n = len(b)
    j = 0      # For index of b
    for i in range(n):
        if a[j] == b[i]:
            j += 1
            if j == m:
                break
    return j == m

# Driver Code
arr1 = [1,4,3,5]
arr2 = [1,2]
if check_subsequence(arr1, arr2):
    print("Yes")
else:
    print("No")



"""

The above program uses the concept of sub-sequences to solve the problem.

A sub-sequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, the sequence 1, 2, 3, 5 is a sub-sequence of the sequence 1, 2, 3, 4, 5.

The function check_subsequence takes two lists a and b as input and checks whether b is a sub-sequence of a or not. It initializes the variables m and n to store the lengths of a and b respectively. It also initializes the variable j to 0, which will be used as an index for the elements of b.

The function then iterates over the elements of b using a for loop. For each element b[i], it checks whether a[j] is equal to b[i]. If they are equal, it increments j by 1. If j becomes equal to m, it means that all the elements of b are present in a in the same order, and hence, b is a sub-sequence of a. In this case, the function returns True. If