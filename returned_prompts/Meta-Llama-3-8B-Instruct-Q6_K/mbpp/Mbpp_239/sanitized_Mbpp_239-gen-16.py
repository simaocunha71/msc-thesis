def get_total_number_of_sequences(m, n):
    def get_sequences(current, length):
        if length == 1:
            return 1
        total = 0
        for i in range(2, min(m, current//2) + 1):
            total += get_sequences(i, length - 1)
        return total
    return get_sequences(2, n)