def is_polite(n):
    def is_polite_number(m):
        sum1 = 0
        sum2 = 0
        for i in range(1, m):
            if m % i == 0:
                sum1 += i
            if i % m == 0:
                sum2 += i
        if sum1 == m and sum2 == m:
            return True
        return False

    count = 0
    i = 1
    while True:
        if is_polite_number(i):
            count += 1
            if count == n:
                return i
        i += 1