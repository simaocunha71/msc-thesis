def min_k(records, k):
    # sort by second element of tuple
    records.sort(key = lambda x: x[1])
    return records[:k]