    if n > m:
        return -1
    else:
        total = (m + n) * (m - n + 1) // 2
        return bin(total >> int(total & 1))[-1::-1]


