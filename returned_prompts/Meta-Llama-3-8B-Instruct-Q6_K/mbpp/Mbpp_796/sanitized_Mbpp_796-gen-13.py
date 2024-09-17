def return_sum(d):
    total = 0
    for value in d.values():
        try:
            total += value
        except TypeError:
            print(f"Skipping non-numeric value: {value}")
    return total