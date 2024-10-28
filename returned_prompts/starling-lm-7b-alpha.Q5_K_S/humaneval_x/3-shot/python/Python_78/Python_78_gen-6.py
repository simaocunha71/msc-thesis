    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_to_decimal = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    def is_prime(num):
        for p in primes:
            if p > num:
                break
            if num % p == 0:
                return False
        return True

    num_hex = "".join(reversed(num.upper()))
    count = 0
    for d in num_hex:
        if is_prime(hex_to_decimal[d]):
            count += 1
    return count


