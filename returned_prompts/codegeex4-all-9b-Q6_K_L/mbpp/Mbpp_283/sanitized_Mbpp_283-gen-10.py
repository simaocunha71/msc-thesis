def validate(n):
    digit_counts = [0] * 10
    for digit in str(n):
        digit_counts[int(digit)] += 1
    for i in range(10):
        if digit_counts[i] > i:
            return False
    return True