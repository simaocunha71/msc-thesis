def get_total_number_of_sequences(m, n):
    # Initialize a list to store the number of sequences for each length
    num_sequences = [0] * (n + 1)
    num_sequences[0] = 1  # There is one sequence of length 0 (the empty sequence)

    # Iterate over each length
    for length in range(1, n + 1):
        # Iterate over each possible starting number
        for start_num in range(1, m + 1):
            # Iterate over each possible previous number
            for prev_num in range(start_num // 2, start_num):
                # Check if the sequence is valid
                if prev_num <= start_num <= m and num_sequences[length - 1] > 0:
                    # Add the number of sequences that can be formed by adding the current number to the previous sequence
                    num_sequences[length] += num_sequences[length - 1]

    return num_sequences[n]