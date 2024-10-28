def get_total_number_of_sequences(m, n):
    if m < 2:
        return 0
    if m == 2:
        return 1
    if m == 3:
        return 2
    if m == 4:
        return 3
    if m == 5:
        return 4
    if m == 6:
        return 5
    if m == 7:
        return 6
    if m == 8:
        return 7
    if m == 9:
        return 8
    if m == 10:
        return 9
    else:
        if n == 1:
            return 1
        else:
            return get_total_number_of_sequences(m, n - 1)