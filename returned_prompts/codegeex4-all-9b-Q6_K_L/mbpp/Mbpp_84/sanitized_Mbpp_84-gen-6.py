def sequence(n):
    if n == 1 or n == 2:
        return n
    else:
        binary = bin(n-1)[2:]
        ones = binary.count('1')
        twos = binary.count('2')
        return sequence(ones) + sequence(twos)