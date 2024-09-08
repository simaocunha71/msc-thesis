def max_val(lst):
    return max([i for i in lst if isinstance(i, int) or isinstance(i, float)])

print(max_val(['Python', 3, 2, 4, 5, 'version']))  # 5

