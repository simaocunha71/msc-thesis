def count_Substrings(s):
    return sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if sum(int(k) for k in s[i:j]) == j - i)