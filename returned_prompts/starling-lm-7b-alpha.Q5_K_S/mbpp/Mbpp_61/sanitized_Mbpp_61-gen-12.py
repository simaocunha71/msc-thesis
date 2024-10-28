def count_Substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        j = i
        sum = 0
        while j < len(s):
            sum += int(s[j])
            if sum == j - i + 1:
                count += 1
            j += 1
    return count