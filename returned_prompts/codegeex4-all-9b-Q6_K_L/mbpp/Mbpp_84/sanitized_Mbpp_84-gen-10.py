def sequence(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 1
    else:
        sequence_list = [1, 1]
        for i in range(2, n):
            sequence_list.append(sequence_list[i-1] + sequence_list[i-2])
        return sequence_list[n-1]