"""
To divide two lists element wise you can use the zip function to iterate over the two lists simultaneously. Then you can use the division operator to divide each element of the two lists. Finally, you can convert the result to a list using the list function. Here is an example:

def div_list(list1, list2):
    return list(list1[i]/list2[i] for i in range(len(list1)))
"""

from __future__ import division
def div_list(list1, list2):
    return [list1[i]/list2[i] for i in range(len(list1))]

# To test the function:
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]

# To check if the function works with different inputs:
print(div_list([3, 4, 5], [1, 2, 3]))  # Expected output: [3.0, 2.0, 1.6666666666666667]
print(div_list([5, 5, 5], [5, 5, 5]))  # Expected output: [1.0, 1.0, 1.0]
print(div_list([1.0, 2.0, 3.0], [0.1, 0.2, 0.3]))  # Expected output: [10.0, 10.0, 10.0]
print(div_list([0, 0, 0], [1, 1, 1]))  # Expected output: [0.0, 0.0, 0.0]
print(div_list([-3, -2, -1], [1, 2, 3]))  # Expected output: [-3.0, -1.5, -1.0]
print(div_list([10000, 10000, 10000], [1, 2, 3]))  # Expected output: [10000.0, 5000