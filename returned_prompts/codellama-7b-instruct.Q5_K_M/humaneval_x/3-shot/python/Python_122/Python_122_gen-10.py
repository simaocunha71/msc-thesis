    arr[:k] = [int(f"{x:.2f}") for x in arr[:k]]
    return sum(arr[:k])


