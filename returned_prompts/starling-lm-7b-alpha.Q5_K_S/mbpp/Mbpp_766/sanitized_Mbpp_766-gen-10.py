def pair_wise(lst):
    out = []
    for i in range(len(lst) - 1):
        out.append((lst[i], lst[i + 1]))
    return out