def count_Substrings(s):
    total = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if sum(int(k) for k in s[i:j]) == len(s[i:j]):
                total += 1
    return total

