    return len(string) > 1 and all(len(string) % i for i in range(2, int(len(string) ** 0.5) + 1))


