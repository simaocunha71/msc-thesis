def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        diff = t[0] - t[1]
        if max_diff < diff:
            max_diff = diff
    return max_diff


# Test
print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))  # Expected: 7
print(max_difference([(3, 10), (3, 3), (4, 3), (3, 2)]))  # Expected: 8
print(max_difference([(3, 3), (3, 3), (3, 3), (3, 3)]))  # Expected: 0



"""
Explanation:
We define a function called max_difference, which takes in a list of tuples called tuples. We initialize a variable called max_diff to 0, which will store the maximum difference between available pairs in the tuples. We then iterate through each tuple in the tuples list using a for loop. For each tuple, we calculate the difference between the first and second element and store it in a variable called diff. We then compare the current diff to the max_diff, and if the diff is greater, we update the max_diff to the diff. After iterating through all the tuples, we return the max_diff, which is the maximum difference between available pairs in the given tuple list.
"""



"""
Test Cases:

Test Case 1:
Input: [(3, 5), (1, 7), (10, 3), (1, 2)]
Expected Output: 7
Explanation: The maximum difference between available pairs in the given tuple list is 7, achieved by the pair (3, 5).

Test Case 2:
Input: [(3, 10), (3, 3), (4, 3), (3, 2)]
Expected Output: 8
Explanation: The maximum difference between available pairs in the given tuple list is 8, achieved by the pair (3, 10).

Test Case 3:
Input: