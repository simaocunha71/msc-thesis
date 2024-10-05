
def get_max_triples(n):
    max_triples = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i * i - i + 1 + j * j - j + 1 + k * k - k + 1 % 3 == 0:
                    max_triples += 1
    return max_triples