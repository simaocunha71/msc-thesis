def sequence(n):
    sequence_list = [1, 2]
    while len(sequence_list) <= n:
        sequence_list.append(sequence_list[-1] + sequence_list[-2])
    return sequence_list[n-1]