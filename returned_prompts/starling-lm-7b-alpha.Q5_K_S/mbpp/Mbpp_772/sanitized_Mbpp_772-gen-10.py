def remove_length(s, k):
    return " ".join(filter(lambda x: len(x) != k, s.split()))