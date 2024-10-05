    // 对 arr 进行排序
    sort.Ints(arr)

    // 对 arr 进行筛选
    for i := range arr {
        if i < k-1 {
            continue
        }

        if arr[i] > arr[k-1] {
            arr[k-1] = arr[i]
        }
    }

    // 返回最大的 k 个数字
    return arr[:k]
}
