def get_total_number_of_sequences(m: int, n: int) -> int:
    count = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            for k in range(1, m+1):
                for l in range(1, m+1):
                    if i >= 2*j and j >= 2*k and k >= 2*l:
                        count += 1
    return count