
    # Loop over the array from the second element to the end
    for i in range(1, len(arr)):
        # If the current element is not greater than the previous one
        if arr[i] < arr[i-1]:
            # Return the index of the current element
            return i-1
    # If no such element is found, return -1
    return -1

# Test cases
print(can_arrange([1,2,4,3,5]))  # Expected output: 2
print(can_arrange([1,2,3]))  # Expected output: -1
print(can_arrange([5,4,3,2,1]))  # Expected output: 0
print(can_arrange([10,5,4,3,2,1]))  # Expected output: 5
print(can_arrange([1,2,4,5,3]))  # Expected output: 4
<jupyter_output>
2
-1
0
5
4
<jupyter_text>
Question 5Given a string s, create a function to return the count of distinct substrings of s.A substring is a contiguous sequence of characters within a string.
<jupyter_code>
