def min_k(records, k):
    sorted_records = sorted(records, key=lambda x: x[1])
    return sorted_records[:k]