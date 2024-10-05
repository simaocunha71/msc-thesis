    def is_multiple_of_3(x):
        return x % 3 == 0

    def count_triples(n):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if is_multiple_of_3(a[i] + a[j] + a[k]):
                        count += 1

        return count

    return count_triples(n)

