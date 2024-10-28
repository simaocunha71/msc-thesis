def decimal_to_binary(n):
    try:
        return bin(int(n))[2:]
    except ValueError:
        return 'Invalid input'