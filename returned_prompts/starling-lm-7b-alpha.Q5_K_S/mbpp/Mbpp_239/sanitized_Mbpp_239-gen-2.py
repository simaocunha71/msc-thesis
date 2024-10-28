def get_total_number_of_sequences(m, n):
    # Initialize result
    result = 0

    # Initialize sequence with 1
    seq = [1]

    # Initialize count of valid sequences
    count = 0

    # Generate all sequences of length n
    while len(seq) < n:
        # Generate next number in the sequence
        new_num = 2 * seq[-1]

        # Check if new_num is valid
        if new_num <= m:
            # Add new_num to sequence
            seq.append(new_num)
            # Increment count
            count += 1
        else:
            # Backtrack and find a valid new_num
            while len(seq) > 0 and new_num > m:
                # Remove last number from sequence
                seq.pop()
                # Reduce count
                count -= 1
                # Generate new_num again
                new_num = 2 * seq[-1]
            # Add new_num to sequence
            seq.append(new_num)
            # Increment count
            count += 1

    # Return count of valid sequences
    result = count

    return result