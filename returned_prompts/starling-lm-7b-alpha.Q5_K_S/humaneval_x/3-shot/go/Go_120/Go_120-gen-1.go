    sort.Ints(arr)
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = arr[len(arr)-1-i]
    }
    return result
}



