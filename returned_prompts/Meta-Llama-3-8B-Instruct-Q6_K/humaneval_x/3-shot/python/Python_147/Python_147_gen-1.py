    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
# Alternative solution using set to store the sum of triples
from collections import defaultdict

def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = a[i] + a[j] + a[k]
                count[total % 3] += 1
    return count[0] * count[1] // 2


