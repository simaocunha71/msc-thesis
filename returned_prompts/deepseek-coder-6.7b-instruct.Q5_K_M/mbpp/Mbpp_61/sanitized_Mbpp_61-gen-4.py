def count_Substrings(s: str) -> int:
    n = len(s)
    count = 0
    for length in range(1, n+1):
        for i in range(n-length+1):
            substring = s[i:i+length]
            if sum(int(digit) for digit in substring) == length:
                count += 1
    return count