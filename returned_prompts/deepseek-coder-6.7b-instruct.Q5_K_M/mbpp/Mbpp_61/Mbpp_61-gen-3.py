
def count_Substrings(s):
    count = 0
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if sum(int(digit) for digit in substring) == length:
                count += 1
    return count

