def get_median(arr1, arr2, n):
    merged = sorted(arr1 + arr2)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]