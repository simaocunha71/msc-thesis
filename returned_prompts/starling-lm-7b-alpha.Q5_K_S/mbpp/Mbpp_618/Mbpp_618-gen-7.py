def div_list(list1,list2):
    assert len(list1)==len(list2), "Lengths of the two lists must be same"
    res=[]
    for i in range(len(list1)):
        res.append(list1[i]/list2[i])
    return res

# Testing
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0],"Test Failed"
print("Test Passed")

"""
Complexity Analysis:
Time: O(n)
Space: O(n)
"""

"""
Explanation:
In the given problem, we need to divide each element of one list with corresponding element of another list and return the resultant list.
As the division of two elements can be done independently, we can use a for loop to iterate over the lists and perform the division.
We initialize an empty list called res to store the results. In each iteration, we divide the current elements of the two input lists and append the result to res.
Finally, we return the resultant list res.

The time complexity of this algorithm is O(n) as we are performing a fixed amount of work for each element in the input lists. The space complexity is also O(n) as we are storing the resultant list in memory.
"""

"""
Alternative Solution:
We can also use list comprehension to make the code more concise and readable. Here is an alternative solution using list comprehension:

def div_list(list1, list2):
    assert len(list1) == len(list2), "Lengths of the two lists must be same"
    return [list1[i]/list2[i] for i in range(len(list1))]

The time and space complexity of this solution remains the same as the previous one.
"""

"""
Explanation of Alternative Solution:
In the alternative solution, we use a list comprehension to create a new list containing the results of the division. The comprehension iterates over the indices of the input lists using the range function, and for each index i, it divides the ith element of list1 by the ith element of list2.