    if n < 4:
        return n
    else:
        mem = [0] * (n + 1)
        mem[0] = 0
        mem[1] = 0
        mem[2] = 2
        mem[3] = 0

        for i in range(4, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3] + mem[i - 4]

        return mem[n]


