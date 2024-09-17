def is_undulating(n):
    n = str(n)
    if len(n) % 2 == 0:
        half = len(n) // 2
        return all(n[i] == n[-i-1] for i in range(half))
    else:
        half = len(n) // 2 + 1
        return all(n[i] == n[-i-1] for i in range(half)) and n[half] == n[-half]