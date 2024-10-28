def get_total_number_of_sequences(m: int, n: int) -> int:
    count = 0
    for i in range(1, m//2+1):
        count += m//i
    return count