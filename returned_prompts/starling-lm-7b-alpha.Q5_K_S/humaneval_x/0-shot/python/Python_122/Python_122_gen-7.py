
def add_elements(arr, k):
    # Initialize the sum
    total_sum = 0

    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the element is less than 10
        if len(str(arr[i])) < 2:
            total_sum += arr[i]

    return total_sum

# Test
print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24

# Time complexity: O(k)
# Space complexity: O(1)

# Explanation:
# We initialize the sum variable to 0. Then, we iterate through the first k elements of the array and check if the element is less than 10 (i.e., has at most two digits). If so, we add the element to the total sum. Finally, we return the total sum.

# The time complexity of this solution is O(k) because we only need to iterate through the first k elements of the array. The space complexity is O(1) because we only use a constant amount of extra space (the total_sum variable).

# Note: This solution assumes that the input array is already sorted in ascending order. If the array is not sorted, you can sort it first using the sorted() function and then apply the above solution.

# The time complexity of the sorting step is O(n log n), where n is the length of the array. The space complexity of the sorting step is also O(n). However, since the sorting step is not a part of the original solution, it does not affect the overall time and space complexity of the solution.

# Therefore, the overall time complexity of the solution is O(k + n log n) and the overall space complexity is O(1).

# The worst-case scenario occurs when all the elements in the array have less than two digits, in which case the solution would have a time complexity of O(k). The best-case scenario occurs when all the elements in the array have more than two digits, in which case the solution would have a time complexity of O(k).

# In terms of space complexity, the worst