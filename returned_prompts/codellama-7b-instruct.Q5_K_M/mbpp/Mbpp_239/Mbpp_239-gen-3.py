
def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    else:
        return n * get_total_number_of_sequences(m, n - 1)


