def get_total_number_of_sequences(m, n):
    # Initialize a list to store the number of sequences for each length
    sequences = [0] * (n + 1)
    sequences[0] = 1  # There is one sequence of length 0

    # Iterate over each length from 1 to n
    for length in range(1, n + 1):
        # Iterate over each possible last element of the sequence
        for last_element in range(1, m + 1):
            # Check if the last element is greater than or equal to twice the previous element
            if last_element >= 2 * sequences[length - 1]:
                # Add the number of sequences of length length - 1 that can be extended by the last element
                sequences[length] += sequences[length - 1]

    return sequences[n]