    # Here is the solution to the problem:
    # The operation can be performed if and only if the maximum element of the array is greater than the minimum element of the array.
    # This is because, if the maximum element is less than the minimum element, no matter how many times we perform the operation, we cannot get a non-decreasing order.
    # So, we just need to check whether the maximum and minimum elements are equal or not.

    max_element = max(arr)
    min_element = min(arr)

    if max_element == min_element:
        return False
    else:
        return True

    # Complexity Analysis:
    # Time complexity: O(n) because we are using the built-in max and min functions which have a time complexity of O(n)
    # Space complexity: O(1) because we are not using any extra space to store the values

# Test Cases:
print(move_one_ball([3, 4, 5, 1, 2]))  # Expected Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Expected Output: False
print(move_one_ball([]))  # Expected Output: True
print(move_one_ball([-1, 2, 3, 4, 5]))  # Expected Output: True
print(move_one_ball([-2, 2, 3, 4, 5]))  # Expected Output: False





# Explanation: 
# In the given problem, we need to determine whether it is possible to get a sorted array by performing a right shift operation any number of times. 
# The right shift operation means shifting all elements of the array to the right by one position. 
# The last element of the array is moved to the starting position, i.e., the 0th index. 
# The problem states that the given array will have unique elements, and the numbers will be randomly ordered. 
# 
# To solve this problem, we can use a simple approach. We need to check whether the maximum element of the array is greater than the minimum element of the array. 
# If the maximum element is greater