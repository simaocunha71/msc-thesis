def number_of_substrings(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            result += 1
    return result