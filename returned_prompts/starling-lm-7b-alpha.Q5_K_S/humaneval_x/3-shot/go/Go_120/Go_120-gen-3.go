    sort.Ints(arr)
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = arr[len(arr)-i-1]
    }
    return result
}



