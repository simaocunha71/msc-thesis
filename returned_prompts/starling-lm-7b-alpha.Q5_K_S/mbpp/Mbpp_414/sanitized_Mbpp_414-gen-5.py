def overlapping(seq1, seq2):
    '''
    Function to check whether any value in a sequence exists in a sequence or not.
    '''
    return False if len(set(seq1) & set(seq2)) == 0 else True