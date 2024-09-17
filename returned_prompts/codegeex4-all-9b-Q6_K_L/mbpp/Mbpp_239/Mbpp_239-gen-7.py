def get_total_number_of_sequences(m: int, n: int) -> int:
    total_sequences = 0
    for i in range(1, m//2+1):
        if m//i >= i:
            total_sequences += 1
    return total_sequences

