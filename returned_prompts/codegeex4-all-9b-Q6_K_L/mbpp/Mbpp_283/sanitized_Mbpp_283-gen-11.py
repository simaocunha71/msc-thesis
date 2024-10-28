def validate(n: int) -> bool:
    freq = {}
    for digit in str(n):
        if digit not in freq:
            freq[digit] = 1
        else:
            freq[digit] += 1

    for digit, count in freq.items():
        if count > int(digit):
            return False
    return True