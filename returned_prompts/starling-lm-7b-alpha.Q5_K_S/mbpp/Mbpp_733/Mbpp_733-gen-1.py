def find_first_occurrence(arr, x):
    if x not in arr:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i]==x:
                return i

# Test
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5)) # 1
# print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 2)) # 0
# print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10)) # -1
# print(find_first_occurrence([], 10)) # -1

"""
The time complexity of this function is O(n), where n is the length of the array.
The space complexity is O(1), as it uses a fixed amount of space to store the result.
"""

"""
Alternative solution:
The time complexity is O(log n) using binary search, but it requires that the input array is sorted.
"""

"""
Another alternative solution:
The time complexity is O(n) using linear search. This solution is simpler and does not require the input array to be sorted. However, it is slower than the first solution if the array is already sorted.
"""

"""
A more efficient solution:
The time complexity is O(log n) using binary search. This solution is suitable if you need to find the first occurrence of a number in a large sorted array. However, it requires the input array to be sorted.
"""

"""
The best solution:
The time complexity is O(log n) using binary search. This solution is suitable if you need to find the first occurrence of a number in a large sorted array. It also requires the input array to be sorted, but it does not require any additional space.
"""

"""
Conclusion:
The best solution depends on the specific requirements of your problem. If you need to find the first occurrence of