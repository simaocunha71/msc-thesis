def union_elements(t1, t2):
    # Combine the tuples
    combined = t1 + t2
    # Remove duplicates and sort
    unique_sorted = sorted(set(combined))
    return tuple(unique_sorted)