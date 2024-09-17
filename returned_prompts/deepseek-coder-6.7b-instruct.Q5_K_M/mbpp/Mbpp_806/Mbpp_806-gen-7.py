
def max_run_uppercase(s):
    max_length = 0
    current_length = 0
    for char in s:
        if char.isupper():
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    return max(max_length, current_length)


