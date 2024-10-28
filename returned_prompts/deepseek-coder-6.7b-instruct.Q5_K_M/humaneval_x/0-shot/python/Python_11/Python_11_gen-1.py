def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

print(string_tuple('010', '110'))

In this answer, we are iterating over the length of each string and comparing the two strings character by character. If the characters are the same, we append a '0' to the result string. If they are not the same, we append a '1'. We then return the result string.

This is a straightforward approach and should work for all inputs.

Note: This function assumes that the input strings are of the same length and consist only of 1s and 0s. If this is not the case, you would need to add error checking to handle these cases.
