def is_samepatterns(patterns_array, sequence_array):
    if len(patterns_array) != len(sequence_array):
        return False
    for i in range(len(patterns_array)):
        if patterns_array[i] != sequence_array[i]:
            return False
    return True