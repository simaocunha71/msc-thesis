def count(lst):
    return sum(1 for item in lst if item)  # 1 for True, 0 for False