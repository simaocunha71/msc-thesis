def get_pairs_count(arr, sum):
    n = len(arr)
    m = [0] * 1000
    twice_count = 0

    for i in range(0, n):
        if (arr[i] < sum):
            m[arr[i]] += 1

    for i in range(0, n):
        twice_count += m[sum - arr[i]]
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    return int(twice_count / 2)

# Test
print(get_pairs_count([1, 1, 1, 1], 2))  # 6

"""
Explanation:
Given an array of integers, count the number of pairs where the sum is equal to a given value.

The approach here is to use a map to store counts of numbers in the array. Then for each element, we calculate the other number that would make the sum. If the other number is in the map, we add its count to the result. If the number is equal to the other number, we subtract 1 from the result because we counted each pair twice.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

"""
This solution works because it counts each pair twice and then divides by 2 at the end to get the actual count of pairs.

Here is a step-by-step walkthrough of the solution:
1. Initialize a map 'm' and a variable 'twice_count' to 0.
2. For each number in the array, increment the count in 'm'.
3. For each number in the array, calculate the other number that would make the sum.
4. If the other number is in 'm', add its count to 'twice_count'.
5. If the number is equal to the other number, subtract 1 from 'twice_count' because we counted each pair twice.
6. Return 'twice_count' divided by 2 to get the actual count of pairs.
"""

# Note: This solution assumes that the numbers in the array are non-negative and the sum is non-negative.
