
def toggle_middle_bits(n):
    if n == 0 or n == 1:
        return n
    else:
        s = bin(n)[2:]
        s = s[0] + ''.join(['1' if s[i] == '0' else '0' for i in range(1, len(s) - 1)]) + s[-1]
        return int(s, 2)


