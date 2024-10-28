    s = string.lower()
    for i in range(len(s)):
        if s[:i+1] == s[:i+1][::-1]:
            return string + s[:i+1][::-1]

    return string + s[::-1]  # If no palindromic suffix found, append the reversed string


