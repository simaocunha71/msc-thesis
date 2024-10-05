    # You can use the following line to import the required modules:
    # from collections import defaultdict, Counter

    # Initialize the result.
    result = 0

    # Count the occurrence of each element in the array using Counter.
    counter = Counter(arr)

    # Iterate over each element in the array.
    for num in arr:
        # If the number is odd, increment the result.
        if counter[num] % 2 != 0:
            result += 1
        # If the number is even, decrement the counter of that number by one.
        counter[num] -= 1

    # Iterate over each element in the array.
    for num in arr:
        # If the number is even, increment the result.
        if counter[num] % 2 == 0:
            result += 1
        # If the number is odd, decrement the counter of that number by one.
        counter[num] -= 1

    return result // 2

# Time Complexity: O(n)
# Space Complexity: O(k), k is the number of unique elements in the array. In the worst case, k can be n.

# Here is a test case to check your function:
# smallest_change([1,2,3,5,4,7,9,6])  # Returns: 4
# smallest_change([1, 2, 3, 4, 3, 2, 2])  # Returns: 1
# smallest_change([1, 2, 3, 2, 1])  # Returns: 0
























```

# Here is a test case to check your function:
# smallest_change([1,2,3,5,4,7,9,6])  # Returns: 4
# smallest_change([1, 2, 3, 4, 3, 2, 2])  # Returns: 1
# smallest_change([1, 2, 3, 2, 1])  # Returns: 0
```