    def is_happy(s):
        if len(s) < 3:
            return False
        letters = set()
        for i in range(len(s)-2):
            if (s[i], s[i+1], s[i+2]) in letters:
                return False
            letters.add((s[i], s[i+1], s[i+2]))
        return True

    return is_happy(s)


































# Here's a detailed explanation of the solution:

# The function is_happy takes a string s as input and checks if the string is happy or not.

# It first checks if the length of the string is less than 3. If it is, it means that the string cannot have 3 consecutive distinct letters and hence, it is not happy. In such cases, the function returns False.

# If the length of the string is 3 or more, the function creates an empty set called letters. This set will be used to store the 3-tuples of consecutive letters in the string.

# The function then iterates through the string using a range starting from 0 and ending at len(s)-2 (the index of the last possible 3-tuple of consecutive letters). It checks if the 3-tuple of letters at index i, i+1, and i+2 is already present in the letters set. If it is, it means that the 3 consecutive letters are not distinct and hence, the string is not happy. In such cases, the function returns False.

# If the function completes the loop without finding any non-distinct 3 consecutive letters, it means that the string is happy. In this case, the function returns True.

# The is_happy function is then called with the input string s and the result is returned as the final output.



































































