def toggle_middle_bits(num):
    if num <= 3:
        return num
    else:
        return (num | (num - 1)) + 1