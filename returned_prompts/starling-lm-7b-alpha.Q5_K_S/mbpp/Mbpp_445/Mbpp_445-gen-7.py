def index_multiplication(t1,t2):
    len1 = len(t1)
    len2 = len(t2)
    if len1!=len2:
        return "Both tuples should be of same length"
    res = []
    for i in range(len1):
        res.append(t1[i]*t2[i])
    return tuple(res)

# Testing the function
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
print("Test case passed")

"""
This function works by first checking if the lengths of the two tuples are equal. If not, it returns a string indicating that both tuples should be of same length. If the lengths are equal, it creates an empty list and then iterates over the tuples. For each index i, it multiplies the i-th element of the first tuple with the i-th element of the second tuple and appends the result to the list. Finally, it converts the list to a tuple and returns it.
"""

"""
To run this code, you can follow these steps:
1. Define the function index_multiplication as shown in the solution.
2. Test the function by calling it with the given tuples as arguments and comparing the result with the expected output. If the result matches the expected output, print "Test case passed". Otherwise, print an error message.
"""

"""
Note that the function assumes that the input tuples are non-empty and have elements of the same data type. If this assumption is not true, the function may raise an error. You can add additional error checking if necessary to handle such cases.
"""

"""
In terms of complexity, the function has a time complexity of O(n), where n is the length of the tuples. This is because it iterates over the tuples once. The space complexity is also O(n), as it creates a new list to store the results.
"""

"""
Overall, this solution provides a