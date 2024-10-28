    # Convert arr into a set to remove duplicates
    s = set(arr)
    # Check if the length of the set is even or odd
    if len(s) % 2 == 0:
        # If the length is even, count the number of even elements in the set
        even_count = sum(i % 2 == 0 for i in s)
        return even_count
    else:
        # If the length is odd, count the number of odd elements in the set
        odd_count = sum(i % 2 == 1 for i in s)
        return odd_count - 1

# Test Cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Expected output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Expected output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Expected output: 0

# Driver Code
smallest_change([1,2,3,5,4,7,9,6])
smallest_change([1, 2, 3, 4, 3, 2, 2])
smallest_change([1, 2, 3, 2, 1])

# This code is contributed by Eesha Singh



















































































































































































