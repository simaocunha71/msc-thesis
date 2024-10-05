    if len(arr) == 0 {
        return true
    }

    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Slice(sorted, func(i, j int) bool {
        return sorted[i] < sorted[j]
    })

    min_index := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] < arr[min_index] {
            min_index = i
        }
    }

    if min_index == 0 {
        return true
    }

    for i := 1; i < len(arr); i++ {
        if arr[(min_index+i)%len(arr)] != sorted[i%len(sorted)] {
            return false
        }
    }

    return true
}