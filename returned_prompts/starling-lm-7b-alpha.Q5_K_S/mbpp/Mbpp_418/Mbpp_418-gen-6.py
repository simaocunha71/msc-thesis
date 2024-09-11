def Find_Max(arr):
    max_ele = arr[0]
    for i in range(1,len(arr)):
        if len(arr[i]) > len(max_ele):
            max_ele = arr[i]
    return max_ele


# Driver Code
Find_Max([['A'],['A','B'],['A','B','C']])
"""
The function works by first assuming the first element of the array to be the maximum element. Then, it iterates through the rest of the array and checks whether each element is longer than the maximum element. If an element is longer, the maximum element is updated. After the iteration, the maximum element is returned.
"""

# Testing
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
print("All Test Cases Passed")


# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Note: This question can also be solved using built-in Python functions, which would result in a more efficient solution. However, the purpose of this question is to demonstrate understanding of Python fundamentals.


# Explanation of Built-In Solution
"""
In Python, we can use the built-in max() function to find the element of a list having maximum length. The max() function returns the maximum value in an iterable or the maximum of two or more arguments.

To find the element of a list having maximum length, we can pass a list of lengths of each element to the max() function. Here's how you can do it:

def Find_Max(arr):
    max_length = max(len(ele) for ele in arr)
    return max_length

In the above code, we use a generator expression to calculate the length of each element in the list. The max() function then returns the maximum length.

The time complexity of this solution is O(n), where n is the number of elements in the list. The auxiliary space required by this solution is O(1), as we are not using any extra space that grows with the size of the input.
"""

# Built-In Solution Testing
assert Find_Max([['A'],['A','B'],['A