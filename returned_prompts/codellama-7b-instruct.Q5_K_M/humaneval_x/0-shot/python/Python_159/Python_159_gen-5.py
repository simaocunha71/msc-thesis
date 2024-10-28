
    total = number + remaining
    if total >= need:
        return [total - need, 0]
    else:
        return [total, need - total]