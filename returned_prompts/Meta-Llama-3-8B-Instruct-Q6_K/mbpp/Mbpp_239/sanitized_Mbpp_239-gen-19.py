def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    count = 0
    for i in range(2, min(m, n*2)+1):
        count += get_total_number_of_sequences(m, n-1)
    return count