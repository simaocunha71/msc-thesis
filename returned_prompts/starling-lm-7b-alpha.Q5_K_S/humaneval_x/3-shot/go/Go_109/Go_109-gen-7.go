    sorted := make([]int,len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)
    for i := range arr {
        if sorted[i] != arr[(i+1)%len(arr)] {
            return false
        }
    }
    return true
}



