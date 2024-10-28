def pos_count(lst):
    return len([i for i in lst if i > 0])  # or return sum(1 for i in lst if i > 0)  # or use sum(1 for i in lst if i > 0) for more concise version