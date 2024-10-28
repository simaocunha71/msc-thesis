def get_median(lst1, lst2, n):
    merged = lst1 + lst2
    merged.sort()

    if n % 2 == 0:  # even number of elements
        median1 = merged[n//2]
        median2 = merged[n//2 - 1]
        return (median1 + median2) / 2
    else:  # odd number of elements
        return merged[n//2]