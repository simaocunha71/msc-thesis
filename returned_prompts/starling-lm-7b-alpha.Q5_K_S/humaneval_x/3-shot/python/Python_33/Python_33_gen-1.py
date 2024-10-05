    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    sorted_third_indices = sorted([l[i] for i in third_indices])

    third_sorted = [sorted_third_indices[i % len(third_indices)] for i in range(len(l)) if i % 3 == 0]
    return [l[i] if i % 3 != 0 else third_sorted[i // 3] for i in range(len(l))]


