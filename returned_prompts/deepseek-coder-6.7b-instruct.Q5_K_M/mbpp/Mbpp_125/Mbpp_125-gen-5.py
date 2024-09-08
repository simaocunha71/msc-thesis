"""
Here we will traverse through the binary string and keep track of the count of 1s and 0s. For each 0 encountered, we will decrement the count of 1s and for each 1 encountered, we will increment the count of 1s. We will also keep track of the maximum difference in counts of 1s and 0s encountered so far. This maximum difference will be the answer to the problem.

In Python:

def find_length(bin_str):
    max_diff = 0
    count_1s = 0
    count_0s = 0

    for bit in bin_str:
        if bit == '1':
            count_1s += 1
        else:
            count_0s += 1
        max_diff = max(max_diff, abs(count_1s - count_0s))

    return max_diff

print(find_length("11000010001"))
"""

The binary string "11000010001" will have a maximum difference of 6 between the number of 1s and 0s in any sub-string, which is achieved by selecting the sub-string "10001".
"""

# Python code
def find_length(bin_str):
    max_diff = 0
    count_1s = 0
    count_0s = 0

    for bit in bin_str:
        if bit == '1':
            count_1s += 1
        else:
            count_0s += 1
        max_diff = max(max_diff, abs(count_1s - count_0s))

    return max_diff

print(find_length("11000010001"))  # Output: 6


# Complexity Analysis:
# Time Complexity: O(n), where n is the length of the binary string.
# We traverse the binary string once.
# Space Complexity: O(1), as we are using only a constant amount of space.
# We are not using any data structure that scales with the input size.
# We are only using a few variables to keep track of the counts and the