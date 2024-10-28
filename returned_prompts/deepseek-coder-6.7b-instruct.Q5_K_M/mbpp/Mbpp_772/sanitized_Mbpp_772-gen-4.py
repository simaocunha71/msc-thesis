def remove_length(s, k):
    s = s.split()
    return ' '.join([i for i in s if len(i) != k])