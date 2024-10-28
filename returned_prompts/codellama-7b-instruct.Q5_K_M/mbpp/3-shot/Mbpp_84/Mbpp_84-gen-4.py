
def sequence(n):
    mem = {1: 1, 2: 2}
    if n in mem:
        return mem[n]
    else:
        mem[n] = sequence(mem[n-1] + mem[n-2])
        return mem[n]


