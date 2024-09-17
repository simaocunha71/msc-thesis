
def count_Substrings(s):
    counter = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum(int(x) for x in substring) == len(substring):
                counter += 1
    return counter


