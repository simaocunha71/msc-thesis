
def add_elements(arr, k):
    sum = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]
    return sum

# Time Complexity: O(n), where n is k.
# Space Complexity: O(1)

# For each element in the given array, we check if the length of the element is less than or equal to 2. If so, we add the element to the sum. Finally, we return the sum.

# The time complexity of this solution is O(n), where n is k, since we iterate through the first k elements of the given array. The space complexity is O(1) since we only use a single variable to store the sum.

# Here's a step-by-step breakdown of the solution:

# 1. Initialize a variable sum to 0, which will store the sum of the elements with at most two digits.
# 2. Iterate through the first k elements of the given array using a for loop.
# 3. For each element, check if the length of the element (converted to a string) is less than or equal to 2. If so, add the element to the sum.
# 4. After iterating through all the elements, return the sum.

# This solution ensures that we only consider the first k elements of the array and only add elements with at most two digits to the sum.

# Here's an example usage of the function:

arr = [111,21,3,4000,5,6,7,8,9]
k = 4
print(add_elements(arr, k))  # Output: 24

# In the given example, we have an array arr = [111,21,3,4000,5,6,7,8,9] and k = 4. The function will iterate through the first 4 elements of the array (111, 21, 3, and 4000) and add the elements with at most two digits (21 and 3) to the sum. The sum of these elements is 24, which is returned by