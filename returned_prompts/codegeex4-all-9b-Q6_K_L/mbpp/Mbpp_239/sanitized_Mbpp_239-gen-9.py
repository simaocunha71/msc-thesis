def get_total_number_of_sequences(m, n):
    def count_sequences(start, length):
        if length == 0:
            return 1
        count = 0
        for i in range(2*start, min(m, 2*start+1)):
            count += count_sequences(i, length-1)
        return count

    return count_sequences(1, n)