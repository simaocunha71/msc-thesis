def remove_length(s, k):
    result = ""
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            if len(s[i:i+k]) != k:
                result += s[i:i+k]
        else:
            result += s[i]
    return result