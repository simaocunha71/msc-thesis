def find_Parity(n):
    try:
        n = int(n)
        if n < 0:
            n = abs(n)
        return bin(n).count('1') % 2 != 0
    except ValueError:
        return "Input must be a positive integer"