def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum(map(int, substring)) == len(substring):
                count += 1
    return count