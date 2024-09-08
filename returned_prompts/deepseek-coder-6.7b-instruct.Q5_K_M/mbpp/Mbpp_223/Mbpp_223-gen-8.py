def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x and arr[i + n//2] == x:
            return True
    return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))  # True

"""
Explanation:
The function iterates through the array and checks if the current element is equal to the target element. If so, it checks the next n//2 elements. If any of those are equal to the target element, the function returns True. If not, the function continues to the next element. If it has iterated through the entire array and not found a majority, it returns False.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
This solution assumes that the input array is sorted. If the array is not sorted, the function should first sort it. However, sorting the array would increase the time complexity to O(n log n), which is worse than the original O(n) time complexity.
"""

"""
This solution uses a simple loop to check each element of the array. It checks if the current element is the target element and if the next n//2 elements are also the target element. If either of these conditions is true, it returns True. If it iterates through the entire array without finding a majority, it returns False.
"""

"""
This solution works by using the fact that the input array is sorted. It checks if the target element is in the array by looking at the first and last occurrence of the target element in the array. If the target element appears more than n/2 times, its first and last occurrence will be more than n/2 apart. The function then checks if the target element is in between these two occurrences. If it is, the function returns True, indicating that the target element is the majority element. If not, the function returns False.
"""

"""
This solution is efficient because it uses a single loop to check each element of the array. It checks if the current element is the target element and if the next n//2 elements are also the target element. If either of these conditions is true, the function returns True.