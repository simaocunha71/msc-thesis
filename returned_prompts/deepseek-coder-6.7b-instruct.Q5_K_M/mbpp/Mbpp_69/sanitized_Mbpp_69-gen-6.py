def is_sublist(larger, smaller):
    return [i for i in range(len(larger)) if larger[i:i+len(smaller)] == smaller]