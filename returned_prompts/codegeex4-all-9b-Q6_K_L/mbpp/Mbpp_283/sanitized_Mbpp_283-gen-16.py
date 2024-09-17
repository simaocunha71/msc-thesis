def validate(num):
    frequency = {}
    for digit in str(num):
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    for digit, count in frequency.items():
        if count > int(digit):
            return False
    return True