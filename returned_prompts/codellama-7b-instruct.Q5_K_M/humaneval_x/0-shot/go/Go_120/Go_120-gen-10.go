    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })

    if k >= len(arr) {
        return arr
    }

    return arr[:k]
}
