
def odd_Equivalent(bin_str, rotations):
    n = len(bin_str)
    bin_str = bin_str + bin_str
    odd_count = 0

    for i in range(rotations):
        odd_count += bin_str[i:n+i].count('1')

    return odd_count

print(odd_Equivalent("011001",6))




# Test cases
# print(odd_Equivalent("011001",6)) # should return 3
# print(odd_Equivalent("111111",4)) # should return 6
# print(odd_Equivalent("000000",10)) # should return 0
# print(odd_Equivalent("101010",8)) # should return 4
# print(odd_Equivalent("110011",5)) # should return 4
# print(odd_Equivalent("010101",7)) # should return 3
# print(odd_Equivalent("100100",6)) # should return 2
# print(odd_Equivalent("001000",8)) # should return 1
# print(odd_Equivalent("111000",7)) # should return 3
# print(odd_Equivalent("000111",6)) # should return 2

# In the given binary string, for each rotation, find the number of 1's.
# The binary string is rotated by appending the string to itself.
# Return the total count of 1's in all rotations.

# For example, for the binary string "011001" and 6 rotations, the binary string becomes "011001011001".
# After 1 rotation, there is 1 1 in the first 6 digits.
# After 2 rotations, there are 2 1's in the first 7 digits.
# After 3 rotations, there are 3 1's in the first 8 digits.
# After 4 rotations,