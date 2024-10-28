
    def smallest_change(arr):
        n = len(arr)
        changes = 0
        for i in range(n//2):
            if arr[i] != arr[n-1-i]:
                changes += 1
        return changes

    print(smallest_change([1,2,3,5,4,7,9,6])) # 4
    print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
    print(smallest_change([1, 2, 3, 2, 1])) # 0


This solution works by iterating through the first half of the array, comparing each element with the corresponding element from the end of the array. If they are different, we increment the count of changes. The function then returns this count.

The time complexity of this solution is O(n), where n is the length of the input array.

The space complexity is O(1), since we only use a constant amount of space to store the input array and the variables used for the solution.

This solution assumes that the input array is a list of integers. If the input array is not a list of integers, the function will throw a TypeError.
    """
    return smallest_change(arr)

print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0

# This solution works by iterating through the first half of the array, comparing each element with the corresponding element from the end of the array. If they are different, we increment the count of changes. The function then returns this count.

# The time complexity of this solution is O(n), where n is the length of the input array.

# The space complexity is O(1), since we only use a constant amount of space to store the input array and the variables used for the solution.

# This solution assumes that the input array is a list of integers. If the input array is not a list