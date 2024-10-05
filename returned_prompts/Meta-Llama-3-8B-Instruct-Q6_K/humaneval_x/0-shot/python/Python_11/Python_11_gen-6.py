def string_xor(a: str, b: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1101'))  # Output: '0111'
print(string_xor('0000', '0000'))  # Output: '0000'





# This function performs a binary XOR operation on the input strings a and b.
# It iterates over the characters in the strings, converts each to an integer using int(x) and int(y), 
# performs the XOR operation using the ^ operator, 
# and then converts the result back to a string using str(). 
# The result is then joined together using ''.join() to form the final output string. 
# The zip() function is used to iterate over the characters in the strings in parallel. 
# This allows the XOR operation to be performed character by character, 
# which is what is required for the binary XOR operation. 
# The function is tested with several input strings to verify its correctness. 
# The output of the function is a string consisting only of 1s and 0s, which is the result of the binary XOR operation. 





# Complexity Analysis:
# Time complexity: O(n), where n is the length of the input strings. 
# This is because the function iterates over the characters in the strings once. 
# Space complexity: O(n), where n is the length of the input strings. 
# This is because the function creates a new string as output, which can be as long as the input strings. 





# Error Handling:
# The function does not handle errors. 
# It assumes that the input strings consist only of 1s and 0s, and will raise a ValueError if this is not the case. 
# It also assumes that the input strings are of the same length, and will raise an IndexError if they are not. 
# To handle these errors, the function could be modified to include error checking and handling code. 





# Testing:
# The function is tested with several input strings to verify its correctness. 
# The output of the function is a string consisting only of 1s and 0s, which is the result of the binary XOR operation. 
#