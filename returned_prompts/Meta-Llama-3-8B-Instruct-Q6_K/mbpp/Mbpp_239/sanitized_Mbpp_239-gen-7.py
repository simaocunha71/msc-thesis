def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    else:
        return 1 + get_total_number_of_sequences(m, n-1) + get_total_number_of_sequences(m//2, n-1) if m//2 >= 2 else 0