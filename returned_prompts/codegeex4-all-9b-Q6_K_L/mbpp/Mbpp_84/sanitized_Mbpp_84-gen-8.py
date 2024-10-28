def sequence(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    sequence_list = [1, 2]
    for i in range(2, n):
        sequence_list.append(sequence_list[sequence_list[i-2]-1] + sequence_list[sequence_list[i-1]-1])
    return sequence_list[n-1]