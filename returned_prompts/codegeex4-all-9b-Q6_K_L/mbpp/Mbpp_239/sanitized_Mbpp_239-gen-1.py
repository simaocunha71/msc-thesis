def get_total_number_of_sequences(m, n):
    # Initialize a list to store the number of sequences of length 1, 2, ..., n
    sequences = [0] * (n + 1)
    # There is only one sequence of length 0 (the empty sequence)
    sequences[0] = 1

    # Iterate over the possible values of the first element in the sequence
    for i in range(1, m + 1):
        # Iterate over the possible lengths of the sequence
        for j in range(1, n + 1):
            # If the current value is greater than or equal to twice the previous value,
            # add the number of sequences of length j-1 to the number of sequences of length j
            if 2 * sequences[j - 1] <= i <= m:
                sequences[j] += sequences[j - 1]

    # Return the number of sequences of length n
    return sequences[n]