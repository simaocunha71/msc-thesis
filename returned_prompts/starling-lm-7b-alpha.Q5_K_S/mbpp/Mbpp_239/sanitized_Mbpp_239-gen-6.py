def get_total_number_of_sequences(m, n):
    def helper(total_sequences, length, max_sequence):
        if length == 0:
            return total_sequences
        else:
            return helper(total_sequences + max_sequence, length - 1, m)
    return helper(0, n, 2)