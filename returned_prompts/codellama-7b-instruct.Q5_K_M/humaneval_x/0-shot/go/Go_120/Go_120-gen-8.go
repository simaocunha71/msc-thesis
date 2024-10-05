    // 排序
    sort.Ints(arr)
    // 倒序
    for i := len(arr) - 1; i >= len(arr) - k; i-- {
        arr[k-1] = arr[i]
        k--
    }
    return arr

}

