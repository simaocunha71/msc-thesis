    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)

    for i := 0; i < len(arr); i++ {
        if arr[i] != sorted[(i+1)%len(arr)] {
            return false
        }
    }
    return true
}



