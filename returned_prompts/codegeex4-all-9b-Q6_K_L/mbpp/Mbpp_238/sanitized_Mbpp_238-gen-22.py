def number_of_substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            count += 1
    return count