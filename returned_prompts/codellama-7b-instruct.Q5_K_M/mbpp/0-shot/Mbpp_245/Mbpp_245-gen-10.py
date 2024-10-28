
def max_sum(arr):
    return max(
        [
            sum(arr[i:j])
            for i in range(len(arr))
            for j in range(i + 1, len(arr))
            if all(arr[i] < arr[k] < arr[j] for k in range(i, j))
        ]
    )

