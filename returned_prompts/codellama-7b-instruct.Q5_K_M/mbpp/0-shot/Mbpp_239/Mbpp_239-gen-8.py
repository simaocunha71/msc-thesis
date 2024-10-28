"""
def get_total_number_of_sequences(m, n):
    # Calculate the number of sequences for the first i elements
    # where i is the number of elements in the sequence
    def get_number_of_sequences(i, m, n):
        if i == n:
            return 1
        total = 0
        for j in range(1, m + 1):
            if j >= 2**(i - 1):
                total += get_number_of_sequences(i + 1, m, n)
        return total
    
    # Return the total number of sequences
    return get_number_of_sequences(1, m, n)
"""