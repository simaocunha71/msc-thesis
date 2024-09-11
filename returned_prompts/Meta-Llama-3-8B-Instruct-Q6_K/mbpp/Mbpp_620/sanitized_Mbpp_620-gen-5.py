def largest_subset(lst):
    n = len(lst)
    max_size = 0
    for i in range(1 << n):
        subset = [lst[j] for j in range(n) if (i & (1 << j))]
        if all(i % j == 0 for i in subset for j in subset if i != j):
            max_size = max(max_size, len(subset))
    return max_size