    def is_divisible_by_3(n):
        return n % 3 == 0

    def get_triples(n):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                for k in range(j + 1, len(a)):
                    if is_divisible_by_3(a[i] + a[j] + a[k]):
                        count += 1

        return count

    return get_triples(n)

