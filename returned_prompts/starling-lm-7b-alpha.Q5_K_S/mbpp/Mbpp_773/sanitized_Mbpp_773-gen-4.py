def occurance_substring(string, sub):
    # Initialize result
    result = None

    # Check for all occurrence of substring
    for i in range(len(string)):
        # If found, store the substring and its starting and ending position
        if string[i:i+len(sub)] == sub:
            result = (sub, i, i+len(sub)-1)

    # Return the result
    return result