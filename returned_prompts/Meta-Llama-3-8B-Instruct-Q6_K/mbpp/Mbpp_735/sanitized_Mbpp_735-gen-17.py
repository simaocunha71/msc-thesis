def toggle_middle_bits(n):
    if n < 10:
        return n
    else:
        n = bin(n)[2:]
        middle = len(n) // 2
        result = n[0] + ''.join('1' if bit == '0' else '0' for bit in n[1:middle]) + '0' + ''.join('1' if bit == '0' else '0' for bit in n[middle+1:-1]) + n[-1]
        return int(result, 2)