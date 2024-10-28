    value = float(value)
    if value < 0:
        return int(value) if abs(value) - abs(int(value)) < 0.5 else int(value) - 1
    else:
        return int(value) if abs(value) - abs(int(value)) < 0.5 else int(value) + 1


