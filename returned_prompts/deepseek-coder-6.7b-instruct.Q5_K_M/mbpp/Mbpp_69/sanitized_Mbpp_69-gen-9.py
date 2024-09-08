def is_sublist(l1, l2):
    return [i for i in range(len(l1)) if l1[i:i+len(l2)] == l2]