    neg_numbers = [i for i in lst if i < 0]
    pos_numbers = [i for i in lst if i > 0]

    return (max(neg_numbers) if neg_numbers else None, min(pos_numbers) if pos_numbers else None)


