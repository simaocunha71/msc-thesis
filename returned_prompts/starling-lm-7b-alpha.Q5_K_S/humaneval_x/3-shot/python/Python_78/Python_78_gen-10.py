    prime_hex_map = {
        "2", "3", "5", "7", "B", "D", "F"
    }

    hex_digits = [d for d in num if d.isalpha() or d.isnumeric()]
    count = 0
    for d in hex_digits:
        if d in prime_hex_map:
            count += 1

    return count


