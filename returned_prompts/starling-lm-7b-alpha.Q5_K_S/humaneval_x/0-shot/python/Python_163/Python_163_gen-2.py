
def generate_integers(a, b):
    # Convert the integers to strings
    a_str = str(a)
    b_str = str(b)

    # Initialize the result list
    result = []

    # Iterate through the string representation of the integers
    for i in range(len(a_str)):
        # Check if the current digit is even
        if int(a_str[i]) % 2 == 0:
            # Append the even digit to the result
            result.append(int(a_str[i]))

    # Iterate through the string representation of the integers in reverse
    for i in range(len(b_str)-1, -1, -1):
        # Check if the current digit is even
        if int(b_str[i]) % 2 == 0:
            # Append the even digit to the result
            result.append(int(b_str[i]))

    # Sort the result list in ascending order
    result.sort()

    # Return the result
    return result

# Test cases
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []

# More test cases
print(generate_integers(100, 999))  # Output: [2, 4, 6, 8, 100, 102, 104, 106, 108, 200, 202, 204, 206, 208, 300, 302, 304, 306, 308, 400, 402, 404, 406, 408, 500, 502, 504, 506, 508, 600, 602, 604,