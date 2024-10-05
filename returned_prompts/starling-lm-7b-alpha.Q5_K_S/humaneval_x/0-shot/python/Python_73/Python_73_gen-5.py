    # Make a deep copy of the array
    arr_copy = arr[:]
    arr_copy.sort()

    # Create a dictionary to map the sorted values to their original indices
    mapping = {}
    for i in range(len(arr)):
        mapping[arr_copy[i]] = i

    # Create a set of all unique values in the array
    unique_values = set(arr_copy)

    # Initialize the answer
    ans = 0

    # Iterate over all unique values in the array
    for val in unique_values:
        # If the left and right indices do not match, increment the answer
        if mapping[val] != len(arr) - mapping[val] - 1:
            ans += 1

    # Return the answer
    return ans

# Time: O(n * log(n))
# Space: O(n)


# Test Cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
print(smallest_change([1, 2, 3, 2, 1]))  # 0




















































































































































































































