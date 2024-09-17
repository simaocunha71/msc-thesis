def get_total_number_of_sequences(m, n):
    # base case
    if n == 1:
        return m

    # recursive case
    return sum(get_total_number_of_sequences(m, i) for i in range(1, n)) + 1