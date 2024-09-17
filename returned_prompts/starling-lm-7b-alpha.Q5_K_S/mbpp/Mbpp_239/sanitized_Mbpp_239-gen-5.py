def get_total_number_of_sequences(m, n):
    count = 0
    for i in range(1, m+1):
        if i > m:
            break
        count += 1
        for _ in range(1, n):
            if i * 2 > m:
                break
            if i * 2 > i:
                count += 1
            i *= 2
    return count