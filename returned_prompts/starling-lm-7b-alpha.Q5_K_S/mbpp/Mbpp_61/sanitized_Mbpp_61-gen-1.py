def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if len(str(int(s[i:j]) + int(s[i:j]))) == j - i:
                count += 1
    return count