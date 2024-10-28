def validate(n):
    freq_dict = {}
    for digit in str(n):
        if digit in freq_dict:
            freq_dict[digit] += 1
        else:
            freq_dict[digit] = 1

    for digit, freq in freq_dict.items():
        if freq > int(digit):
            return False
    return True

