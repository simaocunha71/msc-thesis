def find_min_diff(arr: list, n: int) -> int:
    arr.sort()
    return min(arr[i+1] - arr[i] for i in range(n-1))