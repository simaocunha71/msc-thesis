
def count_samepair(l1, l2, l3):
    return sum(1 for i in range(len(l1)) if l1[i]==l2[i]==l3[i])

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))

# Output: 3

"""
Explanation:
The first pair of identical items in the same position is (2, 2, 2) and the last pair is (6, 6, 6). So, the answer is 3.
"""

# 2. Write a Python program to find the longest common prefix string from a list of strings.

