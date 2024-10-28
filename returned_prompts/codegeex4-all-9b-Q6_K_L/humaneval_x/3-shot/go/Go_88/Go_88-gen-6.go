    sorted := make([]int, len(array))

    if (array[0] + array[len(array)-1]) % 2 == 0 {
        copy(sorted, array)
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] > sorted[j]
        })
    } else {
        copy(sorted, array)
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
    }

    return sorted
}



