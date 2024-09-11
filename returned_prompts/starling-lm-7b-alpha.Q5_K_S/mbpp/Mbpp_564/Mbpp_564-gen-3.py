def count_Pairs(arr,n):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]!=arr[j]):
                count+=1
    return count

# Driver code
print(count_Pairs([1,2,1],3))
"""
This function first initializes a count variable to zero. Then it iterates through the range of the length of the array. For each iteration, it uses a nested loop to iterate through the array starting from the next index of the outer loop. If the elements of the array at the two indices are unequal, the count is incremented. Finally, the count is returned as the result.
"""

# Test Case
assert count_Pairs([1,2,1],3) == 2

# This test case checks if the function correctly counts the number of unordered pairs where both elements are unequal in the given list of integers.

"""
In the given test case, the function is called with the list [1,2,1] and the integer 3. The function correctly counts the number of unordered pairs where both elements are unequal, which is 2. The assert statement checks if the function's result is equal to the expected result, which is 2 in this case. If the assert statement passes, it means that the function is correct and the test case is successful.
"""

# This is the expected output of the function for the given test case: 2
# This means that there are 2 possible unordered pairs where both elements are unequal in the list [1,2,1].

# The function correctly counts the number of unordered pairs where both elements are unequal in the given list of integers, and the test case passes.

# The assert statement checks if the function's result is equal to the expected result, and if it is, the test case is successful.

# The function correctly counts the number of unordered pairs where both elements are unequal in the given list of integers, and the test case is successful.

"""
This is a Python function that counts the number of possible unordered pairs where both elements are unequal in a given list of integers. The function takes a list of integers