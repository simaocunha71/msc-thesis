def solve(N):
    return bin(N).count('1')

# The bin() function converts an integer number to a binary string prefixed with "0b".
# The count() function returns the number of occurrences of a substring in a string.
# So, bin(N).count('1') will return the sum of digits in the binary representation of N.