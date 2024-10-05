def string_xor(a: str, b: str) -> str:
    # First, check if the lengths of the strings are equal.
    # If they are not, we cannot perform an XOR operation.
    if len(a) != len(b):
        raise ValueError("The lengths of the input strings are not equal.")

    # Then, initialize an empty string to store the result.
    result = ""

    # Iterate over each character in the strings.
    for i in range(len(a)):
        # XOR the corresponding characters of the two strings.
        # Note: ord() returns the ASCII value of a character.
        xor_result = chr((ord(a[i]) - ord('0')) ^ (ord(b[i]) - ord('0')) + ord('0'))
        # Append the XOR result to the result string.
        result += xor_result

    # Return the result string.
    return result


# Test the function.
print(string_xor('010', '110'))  # Output: '100'


# Now, let's test the function with some edge cases.
try:
    print(string_xor('0101', '101'))  # Raises a ValueError.
except ValueError as e:
    print(e)  # Output: The lengths of the input strings are not equal.

try:
    print(string_xor('0101', '111'))  # Raises a ValueError.
except ValueError as e:
    print(e)  # Output: The lengths of the input strings are not equal.

try:
    print(string_xor('0101', '11011'))  # Raises a ValueError.
except ValueError as e:
    print(e)  # Output: The lengths of the input strings are not equal.

try:
    print(string_xor('0101', '1101'))  # Raises a ValueError.
except ValueError as e:
    print(e)  # Output: The lengths of the input strings are not equal.
