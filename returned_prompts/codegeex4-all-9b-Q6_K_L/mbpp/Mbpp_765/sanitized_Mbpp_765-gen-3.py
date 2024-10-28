def is_polite(n):
    def polite_number(n):
        count = 0
        i = 1
        while count < n:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                count += 1
            if count == n:
                return i
            i += 1

    return polite_number(n)