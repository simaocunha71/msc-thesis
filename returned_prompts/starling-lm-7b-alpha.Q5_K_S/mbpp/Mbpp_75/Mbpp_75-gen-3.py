"""
def find_tuples(list_of_tuples, k):
    result = []
    for t in list_of_tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result
"""

# Python3 program to find all tuples
# which have all elements divisible by k
def find_tuples(list_of_tuples, k):
    result = []
    for t in list_of_tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

# Driver Code
list_of_tuples = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
k = 6
print(find_tuples(list_of_tuples, k))

# This code is contributed by m_s_23.




# Time Complexity: O(n)
# Space Complexity: O(1)

"""
In this program, we are using a list of tuples. We are given a number k and have to find all the tuples in which all the elements are divisible by k. We are using the all() function to check if all the elements in the tuple are divisible by k. If the condition is satisfied, the tuple is added to the result list.
"""

















































































































































































