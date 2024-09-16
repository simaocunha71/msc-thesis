def get_max_sum(n):
    mem = [0] * (n + 1)
    mem[1] = 1
    for i in range(2, n + 1):
        mem[i] = max(mem[i // 2] + mem[i // 3] + mem[i // 4] + mem[i // 5], i)
    return mem[n]