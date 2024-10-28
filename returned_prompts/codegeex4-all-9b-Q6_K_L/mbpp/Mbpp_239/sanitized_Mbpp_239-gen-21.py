def get_total_number_of_sequences(m: int, n: int) -> int:
    total = 0
    for i in range(1, m // 2 + 1):
        for j in range(i, m // 2 + 1):
            for k in range(j, m // 2 + 1):
                for l in range(k, m // 2 + 1):
                    if i * 2 <= j <= i * 2 and j * 2 <= k <= j * 2 and k * 2 <= l <= k * 2 and l * 2 <= m:
                        total += 1
    return total