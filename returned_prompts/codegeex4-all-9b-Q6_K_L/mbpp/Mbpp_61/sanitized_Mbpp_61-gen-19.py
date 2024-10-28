def count_Substrings(s: str) -> int:
    def count_digits(n: int) -> int:
        return sum(int(digit) for digit in str(n))

    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if count_digits(int(substring)) == len(substring):
                count += 1
    return count