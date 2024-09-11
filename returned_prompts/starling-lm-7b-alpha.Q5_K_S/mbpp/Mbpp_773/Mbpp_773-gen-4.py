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

# Driver code
if __name__ == "__main__":
    string = 'python programming, python language'
    sub = 'python'
    print(occurance_substring(string, sub))











"""
The above code is incorrect because:

The function occurance_substring does not correctly identify the occurrence and position of the substrings within a string. It only returns the first occurrence of the substring, rather than all occurrences.

The function uses a for loop to iterate through each index in the string. Within the loop, it checks if the substring starting from the current index matches the given substring. If it does, it stores the substring and its starting and ending position in the result variable. However, this only stores the first occurrence of the substring, rather than all occurrences.

To correct the function, you can modify the code to store all occurrences of the substring in a list, rather than just the first occurrence. You can initialize an empty list to store the occurrences, and then add a tuple containing the substring and its starting and ending position to the list for each occurrence found. Finally, you can return the list of occurrences.

Here's an example of how you can correct the function:

def occurance_substring(string, sub):
    # Initialize result
    result = []

    # Check for all occurrence of substring
    for i in range(len(string)):
        # If found, store the substring and its starting and ending position
        if string[i:i+len(sub)] == sub:
            result.append((sub, i, i+len(sub)-1))

    # Return the result
    return result

This version of the function will return a list of tu