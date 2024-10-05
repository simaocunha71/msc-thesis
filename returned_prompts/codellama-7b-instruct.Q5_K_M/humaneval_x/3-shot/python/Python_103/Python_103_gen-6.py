    if n > m:
        return -1
    elif n == m:
        return bin(n)[2:]
    else:
        total = 0
        for i in range(n, m+1):
            total += i
        return bin(total//(m-n+1))[2:]


