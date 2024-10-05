    if n > m:
        return -1
    else:
        avg = (n + m) // 2
        return bin(avg).replace("0b", "")


