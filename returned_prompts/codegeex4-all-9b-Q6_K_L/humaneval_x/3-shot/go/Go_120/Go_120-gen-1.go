    if k == 0 {
        return []int{}
    }
    if k >= len(arr) {
        return arr
    }

    // Sort in descending order
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })

    return arr[:k]
}


